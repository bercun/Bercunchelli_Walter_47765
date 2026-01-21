# Manual de Usuario - Sistema de Recetas Web

## 📖 Índice
1. [Introducción](#introducción)
2. [Acceso al Sistema](#acceso-al-sistema)
3. [Funciones para Usuarios No Registrados](#funciones-para-usuarios-no-registrados)
4. [Funciones para Usuarios Registrados](#funciones-para-usuarios-registrados)
5. [Gestión de Recetas](#gestión-de-recetas)
6. [Gestión de Perfil](#gestión-de-perfil)
7. [Administración de Avatares](#administración-de-avatares)
8. [Gestión de Chefs](#gestión-de-chefs)
9. [Preguntas Frecuentes](#preguntas-frecuentes)

---

## 🌟 Introducción

Bienvenido al **Sistema de Recetas Web**, una plataforma diseñada para amantes de la cocina donde podrás:

- 🍳 Consultar recetas profesionales curadas por administradores
- 👨‍🍳 Crear y compartir tus propias recetas
- 🔍 Buscar recetas por ingredientes
- 👤 Gestionar tu perfil y avatar personalizado
- 🌐 Conectar con otros chefs aficionados

El sistema cuenta con **dos bases de datos de recetas separadas**:
- **RecetasMain**: Recetas profesionales creadas por administradores, verificadas y probadas
- **RecetasUsr**: Recetas creadas por la comunidad de usuarios, donde puedes compartir tus propias creaciones

---

## 🔐 Acceso al Sistema

### Registro de Nuevo Usuario

1. En la página principal, haz clic en el botón **"Registrarse"** o **"Register"**
2. Completa el formulario con los siguientes datos:
   - **Nombre de usuario** (username)
   - **Nombre** (first_name) - opcional
   - **Correo electrónico** (email)
   - **Contraseña** (password1)
   - **Confirmación de contraseña** (password2)
3. Haz clic en **"Registrar"** o **"Enviar"**
4. El sistema te confirmará que el usuario ha sido creado exitosamente
5. Ya puedes iniciar sesión con tus credenciales

### Inicio de Sesión

1. Haz clic en el botón **"Iniciar Sesión"** o **"Login"**
2. Ingresa tu **nombre de usuario** y **contraseña**
3. Presiona **"Ingresar"** o **"Login"**
4. Si los datos son correctos, verás un mensaje de bienvenida con tu nombre de usuario

### Cerrar Sesión

1. Cuando hayas terminado, haz clic en **"Cerrar Sesión"** o **"Logout"**
2. El sistema te redirigirá a una página de confirmación de cierre de sesión

---

## 👁️ Funciones para Usuarios No Registrados

Aunque no estés registrado, puedes acceder a varias funciones de consulta:

### Consultar Recetas Profesionales (RecetasMain)

1. En el menú principal, selecciona **"Recetas Main"** o **"Recetas Profesionales"**
2. Verás un listado completo de todas las recetas profesionales disponibles
3. Cada receta muestra:
   - Nombre del plato
   - Tipo de cocina
   - Ingredientes
   - Tiempo de preparación
   - Nivel de dificultad
   - Imagen (si está disponible)

### Buscar Recetas por Ingrediente (RecetasMain)

1. Haz clic en **"Buscar Recetas"** o **"Seek Recetas"**
2. En el campo de búsqueda, ingresa el **ingrediente** que deseas buscar
   - Ejemplo: "tomate", "pollo", "arroz"
3. Haz clic en **"Buscar"**
4. El sistema mostrará todas las recetas que contengan ese ingrediente
5. Los resultados incluyen:
   - Ingrediente buscado
   - Lista de recetas encontradas con todos sus detalles

### Buscar Recetas de Usuarios (RecetasUsr)

1. Selecciona **"Buscar Recetas de Usuarios"** o **"Seek Recetas Usr"**
2. Ingresa el ingrediente en el campo de búsqueda
3. Presiona **"Buscar"**
4. Verás todas las recetas creadas por usuarios que incluyen ese ingrediente

### Página "Acerca de" (About)

- Accede a información sobre el proyecto, su propósito y características
- Conoce más sobre la filosofía del sitio web

---

## 👤 Funciones para Usuarios Registrados

Una vez que inicies sesión, tendrás acceso a funcionalidades adicionales:

---

## 🍲 Gestión de Recetas

### Crear una Receta Personal (RecetasUsr)

Esta es una de las funcionalidades principales para usuarios registrados.

1. **Accede al formulario de creación:**
   - Haz clic en **"Agregar Receta de Usuario"** o **"Add Recetas Usr"**

2. **Completa todos los campos requeridos:**
   - **Nombre del plato** (nom_platosUsr): Máximo 20 caracteres
   - **Ingredientes** (ingredientesUsr): Lista de ingredientes, máximo 100 caracteres
   - **Receta** (recetaUsr): Breve descripción, máximo 100 caracteres
   - **Tiempo de preparación** (tiempoUsr): En minutos (número entero)
   - **Dificultad** (dificultadUsr): Por ejemplo: "Fácil", "Media", "Difícil" (máximo 10 caracteres)
   - **Tipo de cocina** (tipoDeCocinaUsr): Por ejemplo: "Italiana", "Mexicana", "Argentina" (máximo 20 caracteres)
   - **Fuente** (fuenteUsr): Origen de la receta (máximo 30 caracteres)
   - **Procedimiento** (procedimientoUsr): Instrucciones detalladas paso a paso
   - **Imagen** (imagenUsr): *Opcional* - Puedes subir una foto del plato

3. **Envía el formulario:**
   - Haz clic en **"Guardar"** o **"Enviar"**
   - Serás redirigido a la página de inicio con un mensaje de confirmación

### Editar/Actualizar una Receta Personal

1. Ve a la lista de recetas de usuarios
2. Busca tu receta en el listado
3. Haz clic en el botón **"Editar"** o **"Actualizar"** junto a tu receta
4. Se abrirá un formulario con los datos actuales pre-cargados
5. Modifica los campos que desees actualizar
6. Puedes cambiar la imagen si lo deseas
7. Haz clic en **"Guardar Cambios"**
8. La receta se actualizará en la base de datos

### Eliminar una Receta Personal

1. Localiza tu receta en el listado de recetas de usuarios
2. Haz clic en el botón **"Eliminar"** o **"Borrar"**
3. La receta será eliminada de forma permanente
4. El listado se actualizará mostrando las recetas restantes

### Ver Todas las Recetas

1. Accede a **"Recetas Main"** desde el menú
2. Verás un listado completo que incluye:
   - Todas las recetas profesionales (RecetasMain)
   - Todas las recetas de usuarios (RecetasUsr)
3. Puedes identificar fácilmente cada tipo por su etiquetado

---

## 🎨 Gestión de Perfil

### Editar Información Personal

Los usuarios registrados pueden actualizar su información de perfil:

1. **Accede a la edición de perfil:**
   - Haz clic en **"Editar Perfil"** o **"Edit Perfil"**

2. **Campos editables:**
   - **Nombre** (first_name)
   - **Correo electrónico** (email)
   - **Contraseña** (password1 y password2)

3. **Proceso de actualización:**
   - Modifica los campos que desees cambiar
   - Si cambias la contraseña, debes ingresarla dos veces para confirmar
   - Haz clic en **"Guardar Cambios"**
   - El sistema actualizará tu información y te redirigirá a la página de inicio

**⚠️ Importante:** Si cambias tu contraseña, asegúrate de recordarla para futuros inicios de sesión.

---

## 🖼️ Administración de Avatares

El sistema de avatares te permite personalizar tu perfil con imágenes.

### Agregar un Nuevo Avatar

1. **Accede a la función de avatares:**
   - Haz clic en **"Agregar Avatar"** o **"Add Avatar"**

2. **Sube tu imagen:**
   - Selecciona un archivo de imagen desde tu computadora
   - Formatos recomendados: JPG, PNG
   - Haz clic en **"Subir"** o **"Guardar"**

3. **Avatar predeterminado:**
   - Si es tu primer avatar, se activará automáticamente como predeterminado
   - Este avatar aparecerá en tu perfil y en tus publicaciones

### Ver tus Avatares

1. Accede a **"Lista de Avatares"** o **"Avatar List"**
2. Verás todos los avatares que has subido
3. El avatar activo estará marcado claramente
4. Solo puedes ver tus propios avatares (no los de otros usuarios)

### Cambiar de Avatar Activo

1. En la lista de avatares, localiza el avatar que deseas activar
2. Haz clic en **"Activar"** junto al avatar deseado
3. El sistema:
   - Desactivará automáticamente tu avatar anterior
   - Activará el nuevo avatar seleccionado
4. Tu nuevo avatar se mostrará en tu perfil inmediatamente

### Editar un Avatar

1. En la lista de avatares, haz clic en **"Editar"** junto al avatar que deseas cambiar
2. Selecciona una nueva imagen
3. Haz clic en **"Guardar"**
4. La imagen del avatar se actualizará

### Eliminar un Avatar

1. En la lista de avatares, haz clic en **"Borrar"** o **"Eliminar"**
2. Se te pedirá confirmación
3. Confirma la eliminación
4. El avatar será eliminado permanentemente de tu cuenta

**💡 Consejo:** Puedes tener múltiples avatares y cambiar entre ellos según tu preferencia.

---

## 👨‍🍳 Gestión de Chefs

El sistema permite gestionar perfiles de chefs/cocineros. Esta función está disponible para usuarios registrados.

### Ver Lista de Chefs

1. Haz clic en **"Chefs"** o **"Cheffs"** en el menú
2. Verás un listado completo de todos los chefs registrados
3. La información mostrada incluye:
   - Nombre del chef
   - Ciudad de origen
   - Tipo de cocina que practica

### Buscar un Chef

1. Accede a **"Buscar Chef"** o **"Seek Usr"**
2. Ingresa el nombre del chef que buscas
3. Haz clic en **"Buscar"**
4. El sistema mostrará todos los chefs que coincidan con tu búsqueda

### Agregar un Nuevo Chef

Puedes registrar tu perfil como chef o el de otros cocineros:

1. **Acceso al formulario:**
   - Haz clic en **"Agregar Chef"** o **"Add Cheff"** / **"Crear Chef"**

2. **Completa los siguientes datos:**
   - **Nombre** (nombreUsr): Máximo 20 caracteres
   - **Email** (emailUsr): Dirección de correo electrónico
   - **Teléfono** (telfonoUsr): Número telefónico (solo números)
   - **Ciudad** (ciudad): Ciudad de residencia (máximo 20 caracteres)
   - **Edad** (edad): Edad en años (número entero)
   - **Tipo de cocina** (tipoDeCocina): Especialidad culinaria

3. **Guarda la información:**
   - Haz clic en **"Guardar"** o **"Crear"**
   - El perfil del chef se agregará a la base de datos

### Ver Detalles de un Chef

1. En la lista de chefs, haz clic en el nombre o en **"Ver Detalles"**
2. Se abrirá una página con toda la información detallada del chef:
   - Nombre completo
   - Correo electrónico
   - Teléfono de contacto
   - Ciudad
   - Edad
   - Tipo de cocina especializada

### Editar Información de un Chef

1. Accede a la lista de chefs
2. Haz clic en **"Editar"** junto al chef que deseas modificar
3. Se abrirá el formulario con los datos actuales
4. Modifica los campos necesarios
5. Haz clic en **"Guardar Cambios"**
6. La información se actualizará en la base de datos

### Eliminar un Chef

1. En la lista de chefs, localiza el perfil a eliminar
2. Haz clic en **"Borrar"** o **"Eliminar"**
3. Se te pedirá confirmación de la eliminación
4. Confirma la acción
5. El perfil del chef será eliminado permanentemente

---

## 🔧 Funciones Administrativas

### Gestión de Recetas Profesionales (RecetasMain)

Solo usuarios con permisos de administrador pueden:

#### Agregar Recetas Profesionales

1. Accede a **"Agregar Receta Main"** o **"Add Recetas Main"**
2. Completa el formulario con los siguientes datos:
   - **Nombre del plato** (nom_platos): Máximo 20 caracteres
   - **Ingredientes** (ingredientes): Lista detallada, máximo 100 caracteres
   - **Receta** (receta): Breve descripción, máximo 100 caracteres
   - **Tiempo** (tiempo): Tiempo de preparación en minutos
   - **Dificultad** (dificultad): Nivel de dificultad (máximo 10 caracteres)
   - **Tipo de cocina** (tipoDeCocina): Categoría culinaria (máximo 20 caracteres)
   - **Fuente** (fuente): Origen o autor de la receta (máximo 30 caracteres)
   - **Procedimiento** (procedimiento): Instrucciones paso a paso detalladas
   - **Imagen** (imagen): *Opcional* - Foto del plato terminado
3. Haz clic en **"Guardar"**
4. La receta se agregará a la base de datos profesional

#### Editar Recetas Profesionales

1. Localiza la receta en el listado de RecetasMain
2. Haz clic en **"Editar"** o **"Actualizar"**
3. El formulario se abrirá con los datos actuales pre-cargados
4. Modifica los campos necesarios
5. Puedes actualizar la imagen si lo deseas
6. Guarda los cambios
7. La receta se actualizará en la base de datos

#### Eliminar Recetas Profesionales

1. En el listado de RecetasMain, busca la receta a eliminar
2. Haz clic en **"Eliminar"**
3. La receta será eliminada de la base de datos
4. El listado se actualizará automáticamente

---

## 📋 Características de las Recetas

### Información que Contiene Cada Receta

Tanto las recetas profesionales (RecetasMain) como las de usuarios (RecetasUsr) incluyen:

- **Nombre del plato**: Identificación clara del platillo
- **Ingredientes**: Lista completa de ingredientes necesarios
- **Tipo de cocina**: Categoría o estilo culinario (Italiana, Mexicana, Argentina, etc.)
- **Tiempo de preparación**: Duración estimada en minutos
- **Nivel de dificultad**: Clasificación de complejidad
- **Fuente**: Autor u origen de la receta
- **Procedimiento**: Instrucciones detalladas paso a paso
- **Imagen**: Fotografía del plato (opcional)

### Funcionalidad de Búsqueda

La búsqueda de recetas actualmente funciona por **ingredientes**:

- Ingresa un ingrediente en el campo de búsqueda
- El sistema busca ese ingrediente en todas las recetas
- La búsqueda es **insensible a mayúsculas/minúsculas**
- Funciona con **búsqueda parcial** (puedes buscar "tom" y encontrará "tomate")
- Se muestran todas las recetas que contengan ese ingrediente en su lista

**Ejemplo de uso:**
- Buscas: "palta"
- Resultado: Todas las recetas que incluyan palta en sus ingredientes

---

## 💡 Preguntas Frecuentes

### ¿Necesito registrarme para usar el sitio?

No es obligatorio. Puedes consultar recetas y buscar por ingredientes sin registrarte. Sin embargo, para crear tus propias recetas, gestionar tu perfil o interactuar con la comunidad de chefs, necesitas crear una cuenta.

### ¿Cuál es la diferencia entre RecetasMain y RecetasUsr?

- **RecetasMain**: Son recetas profesionales, verificadas y probadas, agregadas por administradores del sitio. Son una base confiable de recetas.
- **RecetasUsr**: Son recetas creadas por la comunidad de usuarios. Cualquier usuario registrado puede agregar sus propias interpretaciones y versiones.

### ¿Puedo modificar cualquier receta?

Actualmente, solo puedes modificar tus propias recetas en RecetasUsr. Las recetas de otros usuarios y las RecetasMain solo pueden ser modificadas por administradores.

### ¿Puedo tener más de un avatar?

Sí, puedes subir múltiples avatares y cambiar entre ellos cuando desees. Solo uno estará activo a la vez.

### ¿Cómo recupero mi contraseña si la olvido?

Actualmente el sistema no incluye recuperación automática de contraseña. Contacta al administrador del sitio si necesitas ayuda.

### ¿Las imágenes son obligatorias en las recetas?

No, las imágenes son opcionales tanto en RecetasMain como en RecetasUsr. Sin embargo, se recomienda incluirlas para que las recetas sean más atractivas.

### ¿Puedo buscar recetas por múltiples ingredientes?

Actualmente la búsqueda funciona con un ingrediente a la vez. En futuras versiones se planea implementar búsqueda por múltiples criterios (ingredientes, tiempo, dificultad, tipo de dieta, etc.).

### ¿Qué hago si encuentro un error en una receta?

Si encuentras un error en una RecetasMain, contacta al administrador. Si es una RecetasUsr, puedes contactar al autor o reportarlo al administrador.

### ¿Puedo eliminar mi cuenta?

Para eliminar tu cuenta y toda tu información, debes contactar al administrador del sitio.

### ¿El sitio es responsive/se adapta a móviles?

El diseño básico es funcional en diferentes dispositivos, aunque está optimizado principalmente para escritorio. Mejoras en responsive design están planificadas para futuras versiones.

---

## 🚀 Mejoras Futuras Planificadas

El proyecto está en constante evolución. Algunas funcionalidades previstas incluyen:

1. **Búsqueda avanzada**: Buscar por múltiples ingredientes y otros criterios (tiempo, dificultad, dieta especial)
2. **Sistema de calificaciones**: Los usuarios podrán valorar y comentar recetas
3. **Favoritos**: Guardar recetas favoritas en tu perfil
4. **Recetas del día**: Destacar recetas seleccionadas diariamente
5. **Permisos granulares**: Los usuarios solo podrán editar sus propias recetas
6. **Filtros de dieta**: Buscar recetas vegetarianas, veganas, sin gluten, etc.
7. **Compartir en redes sociales**: Integración con redes sociales
8. **Impresión de recetas**: Formato optimizado para imprimir
9. **Lista de compras**: Generar lista de compras basada en ingredientes
10. **Conversión de unidades**: Convertir medidas automáticamente

---

## 📞 Soporte y Contacto

Si tienes dudas, sugerencias o encuentras algún problema:

- Consulta primero este manual
- Revisa las preguntas frecuentes
- Contacta al administrador del sitio

---

## 👏 Créditos

**Desarrollador**: Walter Bercunchelli  
**Proyecto**: Entrega Final Curso CoderHouse Python  
**Tecnologías**: Django, Python, SQLite, HTML, CSS, JavaScript

---

**¡Gracias por usar el Sistema de Recetas Web! Esperamos que disfrutes compartiendo y descubriendo nuevas recetas culinarias.** 🍳👨‍🍳🍲

---

*Última actualización: Enero 2026*
