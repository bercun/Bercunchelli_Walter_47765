from django.db import models
from django.contrib.auth.models import User


class DificultadChoices(models.TextChoices):
    FACIL = "FACIL", "Fácil"
    MEDIA = "MEDIA", "Media"
    DIFICIL = "DIFICIL", "Difícil"


class UnidadChoices(models.TextChoices):
    GRAMO = "g", "gramos (g)"
    KILO = "kg", "kilos (kg)"
    ML = "ml", "mililitros (ml)"
    LITRO = "l", "litros (l)"
    UNIDAD = "unidad", "unidades"
    TAZA = "taza", "tazas"
    CDA = "cda", "cucharadas"
    CDTA = "cdta", "cucharaditas"
    PIZCA = "pizca", "pizcas"


# Create your models here.
class RecetasMain(models.Model):


    def __str__(self):
        return f"  {self.nom_platos} -- Tipo de cocina: {self.tipoDeCocina} " 
    
    
    nom_platos = models.CharField(max_length=20)
    ingredientes = models.CharField(max_length=100)
    receta = models.CharField(max_length=100)
    tiempo = models.IntegerField()
    dificultad = models.CharField(max_length=10, choices=DificultadChoices.choices, default=DificultadChoices.MEDIA)
    tipoDeCocina = models.CharField(max_length=20)
    fuente = models.CharField(max_length=30)
    procedimiento = models.TextField()
    imagen = models.ImageField(upload_to="recetas", null=True, blank=True)

    @property
    def dificultad_icon(self):
        return {
            "FACIL": "bi-signal-1",
            "MEDIA": "bi-signal-2",
            "DIFICIL": "bi-signal-3",
        }.get((self.dificultad or "").upper(), "bi-signal-2")

    def get_pasos_lista(self):
        pasos = list(self.pasos.all())
        if pasos:
            return [p.texto for p in pasos]
        return [l.strip() for l in (self.procedimiento or "").splitlines() if l.strip()]

    @property
    def ingredientes_items(self):
        from AppRecetas.costos import parse_ingredientes_texto
        return parse_ingredientes_texto(self.ingredientes)

    @property
    def costo_estimado(self):
        from AppRecetas.costos import calcular_costo
        precios = IngredientePrecio.objects.all()
        return calcular_costo(self.ingredientes_items, precios)
    


class RecetasUsr(models.Model):

    def __str__(self):
        return f"  {self.nom_platosUsr} -- Tipo de cocina: {self.tipoDeCocinaUsr} " 
    
    nom_platosUsr = models.CharField(max_length=20)
    ingredientesUsr = models.CharField(max_length=100)
    recetaUsr = models.CharField(max_length=100)
    tiempoUsr = models.IntegerField()
    dificultadUsr = models.CharField(max_length=10, choices=DificultadChoices.choices, default=DificultadChoices.MEDIA)
    tipoDeCocinaUsr = models.CharField(max_length=20)
    fuenteUsr = models.CharField(max_length=30)
    procedimientoUsr = models.TextField()
    imagenUsr = models.ImageField(upload_to="recetas_usuarios", null=True, blank=True)

    @property
    def dificultad_icon(self):
        return {
            "FACIL": "bi-signal-1",
            "MEDIA": "bi-signal-2",
            "DIFICIL": "bi-signal-3",
        }.get((self.dificultadUsr or "").upper(), "bi-signal-2")

    def get_pasos_lista(self):
        pasos = list(self.pasos.all())
        if pasos:
            return [p.texto for p in pasos]
        return [l.strip() for l in (self.procedimientoUsr or "").splitlines() if l.strip()]

    @property
    def ingredientes_items(self):
        from AppRecetas.costos import parse_ingredientes_texto
        return parse_ingredientes_texto(self.ingredientesUsr)

    @property
    def costo_estimado(self):
        from AppRecetas.costos import calcular_costo
        precios = IngredientePrecio.objects.all()
        return calcular_costo(self.ingredientes_items, precios)



class Cheff(models.Model):

    def __str__(self):
        return f"  {self.nombreUsr} -- Origen : {self.ciudad} " 
    
    nombreUsr = models.CharField(max_length=20)
    emailUsr = models.EmailField()
    telfonoUsr = models.IntegerField()
    ciudad = models.CharField(max_length=20)
    edad = models.IntegerField()
    tipoDeCocina = models.CharField(max_length=20)



class Avatar(models.Model):
    
    def __str__(self):
        return f"  {self.usuario} -- Avatar: {self.image} " 


    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to= "avatares", null=True, blank=True)
    is_active = models.BooleanField(default=False)


class IngredientePrecio(models.Model):
    """Precio global estimado por ingrediente (para costo de receta con texto libre)."""

    def __str__(self):
        return f"{self.nombre} ({self.unidad_base}) ${self.precio_estimado}"

    nombre = models.CharField(max_length=60, unique=True)
    unidad_base = models.CharField(max_length=10, choices=UnidadChoices.choices, default=UnidadChoices.UNIDAD)
    precio_estimado = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    moneda = models.CharField(max_length=5, default="ARS")
    fuente = models.CharField(max_length=60, blank=True, default="")
    updated_at = models.DateTimeField(auto_now=True)


class PasoBase(models.Model):
    class Meta:
        abstract = True
        ordering = ["orden"]

    orden = models.PositiveIntegerField(default=1)
    texto = models.TextField()


class PasoMain(PasoBase):
    def __str__(self):
        return f"Main {self.receta_id} paso {self.orden}"

    receta = models.ForeignKey(RecetasMain, on_delete=models.CASCADE, related_name="pasos")

    class Meta:
        ordering = ["orden"]
        constraints = [
            models.UniqueConstraint(fields=["receta", "orden"], name="uniq_pasomain_receta_orden"),
        ]


class PasoUsr(PasoBase):
    def __str__(self):
        return f"Usr {self.receta_id} paso {self.orden}"

    receta = models.ForeignKey(RecetasUsr, on_delete=models.CASCADE, related_name="pasos")

    class Meta:
        ordering = ["orden"]
        constraints = [
            models.UniqueConstraint(fields=["receta", "orden"], name="uniq_pasousr_receta_orden"),
        ]



