# Manual de Usuario - Sistema de Recetas Web

## 📖 Índice
1. [Introducción](#introducción)
2. [Acceso al Sistema](#acceso-al-sistema)
3. [Funciones para Usuarios No Registrados](#funciones-para-usuarios-no-registrados)
4. [Funciones para Usuarios Registrados](#funciones-para-usuarios-registrados)
5. [Gestión de Recetas](#gestión-de-recetas)
6. [Precios de Ingredientes y Costo Estimado](#precios-de-ingredientes-y-costo-estimado)
7. [Gestión de Perfil](#gestión-de-perfil)
8. [Administración de Avatares](#administración-de-avatares)
9. [Gestión de Chefs](#gestión-de-chefs)
10. [Preguntas Frecuentes](#preguntas-frecuentes)

---

## 🌟 Introducción

Bienvenido al **Sistema de Recetas Web**, una plataforma diseñada para amantes de la cocina donde podrás:

- 🍳 Consultar **Recetas Destacadas** y **Recetas de la Comunidad** en un catálogo unificado
- 👨‍🍳 Crear, editar y compartir tus propias recetas con **pasos de preparación numerados**
- 🔍 Buscar recetas por ingrediente, nombre del plato o tipo de cocina desde cualquier pantalla
- 💰 Consultar el **costo estimado** de cada receta y gestionar precios globales de ingredientes
- 👤 Gestionar tu perfil y múltiples avatares personalizados
- 🌐 Explorar y administrar perfiles de chefs

El sistema cuenta con **dos colecciones de recetas**:
- **Destacadas (`RecetasMain`)**: Recetas curadas/verificadas destacadas en la plataforma
- **Comunidad (`RecetasUsr`)**: Recetas creadas y compartidas por los usuarios

---

## 🔐 Acceso al Sistema

### Registro de Nuevo Usuario

1. En la barra de navegación superior, haz clic en **"Registrarse"**
2. Completa el formulario con los siguientes datos:
   - **Nombre de usuario** (`username`)
   - **Nombre** (`first_name`) - opcional
   - **Correo electrónico** (`email`)
   - **Contraseña** (`password1`)
   - **Confirmación de contraseña** (`password2`)
3. Envía el formulario; el sistema confirmará que el usuario fue creado exitosamente
4. Ya puedes iniciar sesión con tus credenciales

### Inicio de Sesión

1. Haz clic en el botón **"Login"**
2. Ingresa tu **nombre de usuario** y **contraseña**
3. Presiona ingresar; si los datos son correctos, verás tu nombre de usuario (y avatar activo, si tienes uno) en la barra superior

### Cerrar Sesión

1. Abre el menú desplegable de tu usuario en la esquina superior derecha
2. Haz clic en **"Cerrar Sesión"** (en móvil, el botón **"Salir"**)
3. El sistema te redirigirá a la pantalla de confirmación de cierre de sesión

---

## 👁️ Funciones para Usuarios No Registrados

Sin necesidad de iniciar sesión, puedes consultar y buscar recetas:

### Explorar el Catálogo de Recetas

1. En el menú principal, selecciona **"Recetas"**
2. Puedes filtrar la vista mediante las pestañas:
   - **Todas**: Muestra recetas de Comunidad y Destacadas
   - **Comunidad**: Solo recetas creadas por usuarios (`RecetasUsr`)
   - **Destacadas**: Solo recetas destacadas (`RecetasMain`)
3. Cada tarjeta de receta muestra:
   - Imagen del plato (si tiene una cargada)
   - Nombre del plato
   - Tipo de cocina, tiempo de preparación (en minutos) y nivel de dificultad (**Fácil**, **Media** o **Difícil**)
   - Resumen de ingredientes
   - **Costo estimado** (calculado a partir de los precios cargados)
   - Fuente de la receta
   - Desplegable **"Ver procedimiento (N pasos)"** con la lista ordenada de pasos

### Buscar Recetas

Tienes dos formas de buscar:

- **Buscador global / unificado**: Desde la barra de navegación superior o desde la parte superior del catálogo **Recetas**, ingresa un término y presiona **Buscar**. Filtra simultáneamente en **Comunidad** y **Destacadas** por **ingrediente, nombre del plato o tipo de cocina** (insensible a mayúsculas/minúsculas y con coincidencias parciales).
- **Búsqueda avanzada por ingrediente**: Desde el catálogo de Recetas, usa el botón **"Búsqueda avanzada"** en la sección de Comunidad o Destacadas para buscar específicamente por ingrediente en cada colección.

### Página "About"

- Accede desde **"About"** en el menú principal para conocer información sobre el proyecto y su filosofía.

---

## 👤 Funciones para Usuarios Registrados

Al iniciar sesión, además de consultar y buscar, tendrás acceso a:

- Crear, editar y eliminar recetas (tanto de **Comunidad** como **Destacadas**)
- Gestionar el catálogo global de **Precios** de ingredientes
- Acceder a la sección **Cheffs** (listar, ver detalles, buscar, crear, editar y eliminar)
- Editar tu perfil de usuario y administrar tus avatares

---

## 🍲 Gestión de Recetas

### Crear una Receta

1. Ve a **Recetas** en el menú principal y haz clic en **"Crear Receta"** (Comunidad) o **"Crear Destacada"** (Destacadas).
2. Completa los campos del formulario:
   - **Nombre del plato**: Máximo 20 caracteres
   - **Ingredientes**: Máximo 100 caracteres. Para aprovechar el cálculo automático de costos, se recomienda usar el formato:
     `2 kg harina, 3 unidad huevo, 200 ml leche`
     *(El formulario muestra sugerencias de ingredientes que ya tienen precio cargado).*
   - **Receta**: Breve descripción (máximo 100 caracteres)
   - **Tiempo**: Duración estimada en minutos (número entero)
   - **Dificultad**: Selector con opciones **Fácil**, **Media** o **Difícil**
   - **Tipo de cocina**: Ej. Italiana, Mexicana, Argentina (máximo 20 caracteres)
   - **Fuente**: Origen o autor de la receta (máximo 30 caracteres)
   - **Procedimiento**: Descripción general en texto
   - **Pasos de preparación (uno por línea)**: Editor dinámico donde puedes pulsar **"Agregar paso"** para cargar cada paso numerado por separado (o quitar pasos con el ícono de papelera). Si agregas pasos aquí, se guardan ordenados y sincronizados con el procedimiento.
   - **Imagen**: *Opcional* - Foto del plato
3. Guarda el formulario para publicar la receta.

### Editar una Receta

1. En el catálogo de **Recetas**, localiza la receta que deseas modificar.
2. Haz clic en **"Editar"** en la parte inferior de la tarjeta.
3. Modifica los campos, los pasos numerados o la imagen (si subes una nueva, reemplazará la anterior).
4. Guarda los cambios.

### Eliminar una Receta

1. En la tarjeta de la receta, haz clic en **"Eliminar"**.
2. Confirma la acción en el cuadro de diálogo del navegador.
3. La receta (junto con sus pasos asociados) se eliminará de la base de datos.

---

## 💰 Precios de Ingredientes y Costo Estimado

El sistema incluye un módulo de **Precios** (`/AppRecetas/precios/`) que permite estimar automáticamente el costo de cada receta manteniendo los ingredientes como texto libre.

### Cómo Funciona el Cálculo

- El sistema analiza el campo de ingredientes de cada receta (separados por coma, punto y coma o salto de línea), extrayendo cantidad, unidad y nombre.
- Convierte unidades compatibles automáticamente:
  - Peso: `g`, `gr`, `gramo(s)`, `kg`, `kilo(s)`
  - Volumen: `ml`, `mililitro(s)`, `l`, `lt`, `litro(s)`, `taza(s)` (200 ml), `cda`/`cucharada(s)` (15 ml), `cdta`/`cucharadita(s)` (5 ml)
  - Otras: `unidad(es)`/`u`, `pizca(s)`
- Si un ingrediente no tiene precio cargado o su unidad no es convertible respecto al precio base, se contabiliza como **sin precio** en la tarjeta de la receta.

### Gestionar Precios (Usuarios Registrados)

1. Haz clic en **"Precios"** en la barra de navegación.
2. Verás la tabla paginada de ingredientes con su **unidad base**, **precio** (por defecto en `ARS`) y **fuente**.
3. **Agregar precio**: Haz clic en **"Agregar precio"** y completa:
   - **Nombre** (único, máx. 60 caracteres)
   - **Unidad base** (`g`, `kg`, `ml`, `l`, `unidad`, `taza`, `cda`, `cdta`, `pizca`)
   - **Precio estimado**
   - **Moneda** (por defecto `ARS`)
   - **Fuente** (opcional, máx. 60 caracteres)
4. **Editar / Borrar**: Usa los botones **"Editar"** o **"Borrar"** en cada fila de la tabla.

---

## 🎨 Gestión de Perfil

### Editar Información Personal

1. Haz clic en tu usuario en la barra superior y selecciona **"Editar Perfil"**.
2. Puedes actualizar:
   - **Nombre** (`first_name`)
   - **Correo electrónico** (`email`)
   - **Contraseña** (`password1` y `password2`)
3. Guarda los cambios para actualizar tu cuenta.

**⚠️ Importante:** Si cambias tu contraseña, asegúrate de recordarla para futuros inicios de sesión.

---

## 🖼️ Administración de Avatares

El sistema de avatares te permite personalizar tu perfil con imágenes.

### Agregar un Nuevo Avatar

1. En el menú de tu usuario, selecciona **"Agregar Avatar"**.
2. Selecciona un archivo de imagen (JPG, PNG) y súbelo.
3. Si es tu primer avatar, se marcará como **activo** automáticamente y aparecerá en la barra de navegación.

### Ver, Activar, Editar y Eliminar Avatares

1. En el menú de tu usuario, selecciona **"Mis Avatares"**.
2. Solo verás tus propios avatares. Desde allí puedes:
   - **Activar**: Establece ese avatar como el activo (desactiva automáticamente el anterior)
   - **Editar**: Reemplaza la imagen del avatar
   - **Borrar**: Elimina el avatar tras confirmar

---

## 👨‍🍳 Gestión de Chefs

La sección **Cheffs** está disponible para usuarios registrados desde el menú principal.

### Ver Lista y Detalles de Chefs

1. Haz clic en **"Cheffs"** en el menú de navegación.
2. Verás el listado de chefs registrados y podrás acceder al detalle de cada uno con toda su información:
   - Nombre
   - Email
   - Teléfono
   - Ciudad
   - Edad
   - Tipo de cocina

### Buscar, Crear, Editar y Eliminar Chefs

- **Buscar**: Desde la búsqueda de chefs puedes filtrar por nombre (`seekUsr`).
- **Crear**: Completa el formulario con nombre, email, teléfono (numérico), ciudad, edad y tipo de cocina.
- **Editar / Eliminar**: Desde el listado de chefs puedes modificar sus datos o eliminar un registro previa confirmación.

---

## 💡 Preguntas Frecuentes

### ¿Necesito registrarme para usar el sitio?
No para consultar. Puedes explorar el catálogo de **Recetas** (Comunidad y Destacadas) y usar los buscadores sin registrarte. Para crear, editar o eliminar recetas, gestionar precios, administrar chefs o personalizar tu perfil y avatar, debes iniciar sesión.

### ¿Cuál es la diferencia entre Recetas Destacadas y de la Comunidad?
- **Destacadas (`RecetasMain`)**: Recetas curadas/destacadas del sitio, identificadas con ícono de estrella y borde superior ámbar.
- **Comunidad (`RecetasUsr`)**: Recetas aportadas por usuarios de la comunidad.

### ¿Cómo se calcula el costo estimado de una receta?
A partir del texto ingresado en **Ingredientes** y los valores cargados en la sección **Precios**. Si usas el formato `cantidad unidad ingrediente` (por ejemplo: `500 g harina, 2 unidad huevo`), el sistema convierte unidades compatibles y suma el costo total.

### ¿Las imágenes son obligatorias en las recetas?
No, son opcionales. Si no subes una imagen, la tarjeta mostrará un marcador visual por defecto.

### ¿El sitio se adapta a dispositivos móviles?
Sí. La interfaz utiliza **Tailwind CSS** y **Alpine.js** con un diseño responsivo que incluye barra de navegación adaptable y menú desplegable para pantallas pequeñas.

### ¿Cómo recupero mi contraseña si la olvido?
Actualmente el sistema no incluye recuperación automática de contraseña. Contacta al administrador del sitio si necesitas asistencia.

---

## 🚀 Mejoras Futuras Planificadas

1. **Permisos por autoría y rol**: Restringir la edición/eliminación de recetas únicamente a su autor o administradores
2. **Filtros avanzados**: Combinar búsqueda por múltiples ingredientes, tiempo máximo, dificultad y restricciones dietéticas
3. **Sistema de calificaciones y favoritos**: Valorar, comentar y guardar recetas favoritas
4. **Lista de compras**: Generar listas de compras consolidadas a partir de una o varias recetas
5. **Recuperación de contraseña**: Flujo automático por correo electrónico

---

## 👏 Créditos

**Desarrollador**: Walter Bercunchelli  
**Proyecto**: Entrega Final Curso CoderHouse Python  
**Tecnologías**: Django 5.1, Python, SQLite, Pillow, Tailwind CSS, Alpine.js, Bootstrap Icons

---

*Última actualización: Noviembre 2026*
