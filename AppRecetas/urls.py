
from django.urls import path
from AppRecetas.views import *



urlpatterns = [
    path("", inicio, name= "Inicio"),
    path("addRecetasMain/", addRecetasMain, name= "AddRecetasMain"),
    path("addRecetasUsr/", addRecetasUsr, name= "AddRecetasUsr"),
    path("recetasUsr/", vista_recetasUsr, name= "RecetasUsr" ),
    path("recetasMain/", vista_recetasMain, name= "RecetasMain"),
    path("usuarios/", vista_usuario, name= "Usuarios"),
    path("Addusr", addUsuario, name= "Addusr"),


]