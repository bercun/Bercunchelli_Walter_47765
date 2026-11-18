# Registro de cambios

Resumen de las mejoras aplicadas al proyecto en tres fases, con pruebas entre cada una.

Archivos modificados:

- `AppRecetas/models.py`
- `AppRecetas/views.py`
- `AppRecetas/urls.py`
- `AppRecetas/forms.py`
- `AppRecetas/templates/AppRecetas/recetasMain.html`
- `AppRecetas/tests.py`

---

## Fase 1: Rendimiento y consultas

### Costo estimado sin consultas repetidas

- `AppRecetas/models.py`: se agregó `calcular_costo_con_precios(precios)` en `RecetasMain` y `RecetasUsr`.
- `costo_estimado` usa un caché (`_costo_estimado_cache`) si la vista lo asignó; si no, calcula con los precios.
- `AppRecetas/views.py` (`vista_recetasMain`): los precios se cargan **una sola vez** por petición y el costo de cada receta se calcula con esa lista. Antes cada tarjeta ejecutaba `IngredientePrecio.objects.all()`.

### Consultas optimizadas en el catálogo

- `vista_recetasMain` usa `prefetch_related("pasos")` en ambos querysets.
- Solo se cargan las recetas de la pestaña activa (`all`, `usr` o `main`). Los totales se obtienen con `count()`.
- `recetasMain.html`: `get_pasos_lista` se evalúa una vez por tarjeta con `{% with %}` (antes se llamaba dos veces).

### Guardado de pasos en bloque

- `_sync_pasos` (`AppRecetas/views.py`) usa `bulk_create` en lugar de un `create` por cada paso.

---

## Fase 2: Corrección de errores y seguridad

### Edición de perfil (`editarUsuario`)

- Bug corregido: `usr.first_name = ["first_name"]` asignaba una lista literal. Ahora usa `info["first_name"]`.
- Tras cambiar la contraseña se llama a `update_session_auth_hash`, para que la sesión no se cierre.
- Al guardar redirige a `Inicio` (antes renderizaba la plantilla directamente).
- `AppRecetas/forms.py`: se eliminó el campo sin uso `mail` de `EditUsrForm`.

### Rutas de recetas por `pk`

- `AppRecetas/urls.py`: `eliminarRecetasMain`, `updateRecetasMain` ahora usan `<int:pk>` en lugar del nombre del plato. Evita errores cuando hay recetas con el mismo nombre.
- `update_RecetasMain`, `update_RecetasUsr`, `eliminarRecetasUsr` y `eliminarRecetasMain` usan `get_object_or_404`.

### Eliminación solo por POST

- `eliminarRecetasUsr` y `eliminarRecetasMain` tienen `@require_POST`. Una petición `GET` responde `405 Method Not Allowed`.
- Tras eliminar, redirigen a `RecetasMain` (patrón PRG), en lugar de renderizar una plantilla.
- `recetasMain.html`: los botones "Eliminar" son formularios `POST` con `{% csrf_token %}` y confirmación previa en JavaScript.

---

## Fase 3: Pruebas automatizadas

Archivo: `AppRecetas/tests.py` (7 pruebas, todas en verde).

- **`CostosTests`**: normalización de texto, parseo de ingredientes, conversión de unidades y cálculo de costo con ingredientes sin precio.
- **`RendimientoCatalogoTests`**: número fijo de consultas en el catálogo (`assertNumQueries`) y filtrado por pestaña.
- **`SeguridadYBugsTests`**:
  - Edición de usuario: guarda `first_name` y mantiene la sesión.
  - Eliminación: rechaza `GET` con 405 y acepta `POST`.
  - Actualización de recetas por `pk` con nombres duplicados, incluyendo pasos.

Ejecutar las pruebas:

```powershell
.env\Scripts\python.exe manage.py test AppRecetas
```

---

## Pendiente

- En las tarjetas del catálogo, el costo se muestra como `$1000,00000`. Falta aplicar un formato de moneda (por ejemplo, `floatformat`) en `recetasMain.html`.
