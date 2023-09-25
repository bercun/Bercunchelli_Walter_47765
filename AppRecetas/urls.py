
from django.urls import path
from AppRecetas.views import *



urlpatterns = [
    path("", inicio, name= "Inicio"),
    # ingresar datos#######################
    path("addRecetasMain/", addRecetasMain, name= "AddRecetasMain"),
    path("addRecetasUsr/", addRecetasUsr, name= "AddRecetasUsr"),
    path("Addusr/", addUsuario, name= "Addusr"),
    # listar datos##################
    path("recetasUsr/", vista_recetasUsr, name= "RecetasUsr" ),
    path("recetasMain/", vista_recetasMain, name= "RecetasMain"),
    path("usuarios/", vista_usuario, name= "Usuarios"),
    #buscar y mostrar datos###########
    
    path("seekRecetas/", seekRecetas, name= "seekRecetas"),
    path("showRecetas/", showRecetas, name= "showRecetas"),
    
    path("seekRecetasUsr/", seekRecetasUsr, name= "seekRecetasUsr"),
    path("showRecetasUsr/", showRecetasUsr, name= "showRecetasUsr"),
    
    path("seekUsr/", seekUsr, name= "seekUsr"),
    path("showUsr/", showUsr, name= "showUsr"),

]