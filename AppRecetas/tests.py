from decimal import Decimal
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from AppRecetas.costos import calcular_costo, convertir, normalizar, parse_ingredientes_texto
from AppRecetas.models import (
    DificultadChoices,
    IngredientePrecio,
    PasoMain,
    PasoUsr,
    RecetasMain,
    RecetasUsr,
    UnidadChoices,
)


class CostosTests(TestCase):
    def test_normalizar_y_parseo(self):
        self.assertEqual(normalizar("  Azúcar  Blanca "), "azucar blanca")
        items = parse_ingredientes_texto("2 kg harina, 3 unidad huevo, sal")
        self.assertEqual(len(items), 3)
        self.assertEqual(items[0]["nombre_norm"], "harina")
        self.assertEqual(items[0]["cantidad_base"], Decimal("2000"))
        self.assertEqual(items[0]["unidad_base"], "g")
        self.assertEqual(items[2]["unidad_base"], "unidad")

    def test_convertir_y_calcular_costo(self):
        self.assertEqual(convertir(Decimal("500"), "g", "kg"), Decimal("0.500"))
        self.assertIsNone(convertir(Decimal("100"), "g", "unidad"))

        precios = [
            IngredientePrecio(nombre="harina", unidad_base="kg", precio_estimado=Decimal("1000")),
            IngredientePrecio(nombre="huevo", unidad_base="unidad", precio_estimado=Decimal("200")),
        ]
        items = parse_ingredientes_texto("500 g harina, 3 huevo, 100 g cacao")
        res = calcular_costo(items, precios)
        self.assertEqual(res["total"], Decimal("1100.000"))
        self.assertEqual(len(res["detalle"]), 2)
        self.assertEqual(res["faltantes"], ["cacao"])


class RendimientoCatalogoTests(TestCase):
    def setUp(self):
        IngredientePrecio.objects.create(
            nombre="harina",
            unidad_base=UnidadChoices.KILO,
            precio_estimado=Decimal("1000.00"),
        )
        for i in range(6):
            rm = RecetasMain.objects.create(
                nom_platos=f"PlatoMain{i}",
                ingredientes="2 kg harina",
                receta="Desc",
                tiempo=20,
                dificultad=DificultadChoices.FACIL,
                tipoDeCocina="Casera",
                fuente="Chef",
                procedimiento="Paso 1",
            )
            PasoMain.objects.create(receta=rm, orden=1, texto="Mezclar")
            ru = RecetasUsr.objects.create(
                nom_platosUsr=f"PlatoUsr{i}",
                ingredientesUsr="1 kg harina",
                recetaUsr="Desc",
                tiempoUsr=15,
                dificultadUsr=DificultadChoices.MEDIA,
                tipoDeCocinaUsr="Casera",
                fuenteUsr="User",
                procedimientoUsr="Paso 1",
            )
            PasoUsr.objects.create(receta=ru, orden=1, texto="Hornear")

    def test_catalogo_sin_n_plus_1(self):
        with self.assertNumQueries(7):
            resp = self.client.get(reverse("RecetasMain"))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "$2000,00")
        self.assertContains(resp, "$1000,00")

    def test_catalogo_tab_usr_no_consulta_lista_main(self):
        with self.assertNumQueries(5):
            resp = self.client.get(reverse("RecetasMain") + "?tab=usr")
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "PlatoUsr0")


class SeguridadYBugsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="cocinero",
            email="old@example.com",
            password="OldPassword123!",
            first_name="OldName",
        )
        self.client.force_login(self.user)

    def test_editar_usuario_guarda_first_name_y_mantiene_sesion(self):
        resp = self.client.post(
            reverse("EditUsr"),
            {
                "first_name": "Walter",
                "email": "new@example.com",
                "password1": "NewPassword456!",
                "password2": "NewPassword456!",
            },
        )
        self.assertRedirects(resp, reverse("Inicio"))
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, "Walter")
        self.assertEqual(self.user.email, "new@example.com")
        self.assertTrue(self.user.check_password("NewPassword456!"))
        # La sesión sigue autenticada tras cambiar la contraseña
        self.assertIn("_auth_user_id", self.client.session)

    def test_eliminar_recetas_requiere_post_y_usa_pk(self):
        rm = RecetasMain.objects.create(
            nom_platos="Repetido",
            ingredientes="1 kg harina",
            receta="Desc",
            tiempo=10,
            dificultad=DificultadChoices.FACIL,
            tipoDeCocina="Casera",
            fuente="Chef",
            procedimiento="P1",
        )
        ru = RecetasUsr.objects.create(
            nom_platosUsr="Tarta",
            ingredientesUsr="2 huevo",
            recetaUsr="Desc",
            tiempoUsr=25,
            dificultadUsr=DificultadChoices.MEDIA,
            tipoDeCocinaUsr="Dulce",
            fuenteUsr="User",
            procedimientoUsr="P1",
        )

        # GET debe ser rechazado con 405 Method Not Allowed
        self.assertEqual(self.client.get(reverse("eliminarRecetasMain", args=[rm.pk])).status_code, 405)
        self.assertEqual(self.client.get(reverse("eliminarRecetasUsr", args=[ru.pk])).status_code, 405)
        self.assertTrue(RecetasMain.objects.filter(pk=rm.pk).exists())
        self.assertTrue(RecetasUsr.objects.filter(pk=ru.pk).exists())

        # POST elimina y redirige a RecetasMain
        resp_main = self.client.post(reverse("eliminarRecetasMain", args=[rm.pk]))
        resp_usr = self.client.post(reverse("eliminarRecetasUsr", args=[ru.pk]))
        self.assertRedirects(resp_main, reverse("RecetasMain"))
        self.assertRedirects(resp_usr, reverse("RecetasMain"))
        self.assertFalse(RecetasMain.objects.filter(pk=rm.pk).exists())
        self.assertFalse(RecetasUsr.objects.filter(pk=ru.pk).exists())

    def test_update_recetas_main_por_pk_con_nombres_duplicados_y_pasos(self):
        rm1 = RecetasMain.objects.create(
            nom_platos="Pizza",
            ingredientes="500 g harina",
            receta="Clasica",
            tiempo=30,
            dificultad=DificultadChoices.FACIL,
            tipoDeCocina="Italiana",
            fuente="Chef",
            procedimiento="Amasar",
        )
        rm2 = RecetasMain.objects.create(
            nom_platos="Pizza",
            ingredientes="500 g harina",
            receta="Fugazzeta",
            tiempo=35,
            dificultad=DificultadChoices.MEDIA,
            tipoDeCocina="Argentina",
            fuente="Chef",
            procedimiento="Amasar",
        )
        resp = self.client.post(
            reverse("updateRecetasMain", args=[rm2.pk]),
            {
                "nom_platos": "Pizza",
                "ingredientes": "500 g harina",
                "receta": "Fugazzeta rellena",
                "tiempo": 40,
                "dificultad": DificultadChoices.DIFICIL,
                "tipoDeCocina": "Argentina",
                "fuente": "Chef",
                "procedimiento": "Amasar",
                "paso_texto": ["Amasar 10 min", "Agregar cebolla y queso", "Hornear"],
            },
        )
        self.assertEqual(resp.status_code, 200)
        rm1.refresh_from_db()
        rm2.refresh_from_db()
        self.assertEqual(rm1.receta, "Clasica")
        self.assertEqual(rm2.receta, "Fugazzeta rellena")
        self.assertEqual(rm2.get_pasos_lista(), ["Amasar 10 min", "Agregar cebolla y queso", "Hornear"])
