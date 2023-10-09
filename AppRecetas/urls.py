
from django.urls import path
from AppRecetas.views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [
    
    #inicio de sesion
    path("login/", inicioDeSesion, name= "Login"),
    path("register/", register, name= "Register"),
    path("logout/", LogoutView.as_view(template_name="AppRecetas/logout.html"), name= "Logout"),
    path( "editUsr/", editarUsuario, name= "EditUsr"),
    
    
    path("", inicio, name= "Inicio"),
    # ingresar datos#######################
    path("addRecetasMain/", addRecetasMain, name= "AddRecetasMain"),
    path("addRecetasUsr/", addRecetasUsr, name= "AddRecetasUsr"),
    path("Addusr/", addUsuario, name= "Addusr"),
    # listar datos##################
    path("recetasUsr/", vista_recetasUsr, name= "RecetasUsr"),
    path("recetasMain/", vista_recetasMain, name= "RecetasMain"),
    path("usuarios/", vista_usuarios, name= "Usuarios"),
    #buscar y mostrar datos###########
    
    path("seekRecetas/", seekRecetas, name= "seekRecetas"),
    path("showRecetas/", showRecetas, name= "showRecetas"),
    
    path("seekRecetasUsr/", seekRecetasUsr, name= "seekRecetasUsr"),
    path("showRecetasUsr/", showRecetasUsr, name= "showRecetasUsr"),
    
    path("seekUsr/", seekUsr, name= "seekUsr"),
    path("showUsr/", showUsr, name= "showUsr"),
    # editar y borrar modelos
    path("eliminarRecetasUsr/<nom_recetasUsr>/", eliminarRecetasUsr, name="eliminarRecetasUsr"),
    path("eliminarRecetasMain/<recetas>/", eliminarRecetasMain, name="eliminarRecetasMain"),
    path("updateRecetasMain/<recetas>/", update_RecetasMain, name="updateRecetasMain"),
    path("updateRecetasUsr/<recetasUsr>/", update_RecetasUsr, name="updateRecetasUsr"),
  # editar con classes
    path("usuario/list/", ListaUsuario.as_view(), name="listaUsuario"),
    path("usuario/<int:pk>/", DetalleUsuario.as_view(), name="detalleUsuario"),
    path("usuario/crear/", CrearUsuario.as_view(), name="crearUsuario"),
    path("usuario/editar/<int:pk>/", UpdateUsuario.as_view(), name="updateUsuario"),
     path("usuario/borrar/<int:pk>/", BorrarUsuario.as_view(), name="borrarUsuario"),
  
  
  ] 