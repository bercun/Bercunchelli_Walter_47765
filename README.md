# Entrega final curso Coder House Python

Este es un readme, que explica en normas generales el uso y como cree este proyecto Web en django

En principio agradecerles por el tiempo que dediquen a evaluar y ver este proyecto

Esta pagina esta orientada el mundo de la cocina

Fue creada una base de datos sqlite, que le agregue 4 modelos " RecetasMain, RecetasUsr, Cheffs y  Usuarios"

La idea es crear dos BD de recetas de cocina, aisladas entre ellas, la primera "RecetasMain"  serian recetas sólo ingresadas por el administrador del sitio, pueden ser vista por todos pero solo modificadas por el administrador (esto ultimo seria agragado en la siguient version)
Luego la segunda BD "RecetasUsr" seria creada por los usuarios y modificada solo por el que la creo pero vista por todos los usuarios(la opcion de modificar solo por el creador me falta estaria pronta de futuras versiones)

Esta diferencia sería para tener unas recetas base ya probadas (RecetasMain), pero darle oportunidad para que los usuarios creen sus versiones e interpretaciones de las recetas

En la pagina principal, están los botones para: crear nuevas instancias en las bases de datos, para buscar por ingrediente y en un futuro un boton para que te muestre las recetas del día o las últimas modificadas o actualizadas

Al crear las base datos de recetas le di como parametros: nombre de plato, ingrediente, tiempo de preparación, dificultad, tipo de cocina, fuente, procedimeinto

La busqueda por el momento solo se hace por ingrediente, pero la idea es cruzar parametros, por ejempo :  estoy en casa y tengo , tomate, palta y cebolla, ademas tengo poco tiempo y soy celiaco,  entnces seria buscar en las recetas las que tengan mayor datos en comun con la busqueda 

El frontend es muy basico que al ser mi primer pagina me falta conocimiento de diseño, pero es funcional, en lo que se refiere a dar de alta instancias en la base de datos , realizar busqueda en dicha base de datos, el login y diferenciar opciones para usuarios logueado o no  

Los datos de superuser son:  usuario : bercun passord : 1234

Muchas gracias por su tiempo

Walter Bercunchelli 
