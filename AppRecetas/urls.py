
from django.urls import path
from AppRecetas.views import *



urlpatterns = [
    path("", inicio, name= "Inicio"),
    path("addrecetasMain/", addRecetasMain, name= "AddrecetasMain"),
    path("addrecetasUsr/", addRecetasUsr, name= "AddRecetasUsr"),
    path("recetasUsr/", vista_recetasUsr, name= "RecetasUsr" ),
    path("recetasMain/", vista_recetasMain, name= "RecetasMain"),
    path("usuarios/", vista_usuario, name= "Usuarios"),



]