
from django.urls import path
from AppRecetas.views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [
    
    #inicio de sesion
    path("login/", inicioDeSesion, name= "Login"),
    path("register/", register, name= "Register"),
    path("logout/", LogoutView.as_view(template_name="AppRecetas/logout.html"), name= "Logout"),
    path("editUsr/", editarUsuario, name= "EditUsr"),
    path("addAvatar/", addAvatar, name= "AddAvatar"),
    
    #avatares con class

    path("avatar/list/", ListaAvatar.as_view(), name="listaavatar"), 
    #path("avatar/crear/", CrearAvatar.as_view(), name="crearAvatar"),
    
    
    path("", inicio, name= "Inicio"),
    path("about/", about, name= "About"),
    path("base/", test, name= "Test"),
    
    
    # ingresar datos#######################
    path("addRecetasMain/", addRecetasMain, name= "AddRecetasMain"),
    path("addRecetasUsr/", addRecetasUsr, name= "AddRecetasUsr"),
    path("AddCheff/", addCheff, name= "AddCheff"),
    # listar datos##################
    path("recetasUsr/", vista_recetasUsr, name= "RecetasUsr"),
    path("recetasMain/", vista_recetasMain, name= "RecetasMain"),
    path("cheffs/", vista_cheffs, name= "Cheffs"),
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
    path("cheff/list/", ListaCheff.as_view(), name="listaCheff"),
    path("cheff/<int:pk>/", DetalleCheff.as_view(), name="detalleCheff"),
    path("cheff/crear/", CrearCheff.as_view(), name="crearCheff"),
    path("cheff/editar/<int:pk>/", UpdateCheff.as_view(), name="updateCheff"),
     path("cheff/borrar/<int:pk>/", BorrarCheff.as_view(), name="borrarCheff"),
  
  
  ] 