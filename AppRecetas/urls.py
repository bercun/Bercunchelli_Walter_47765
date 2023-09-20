
from django.urls import path
from AppRecetas.views import *



urlpatterns = [
    path("", inicio),
    path("addrecetasMain/", addRecetasMain),
    path("addrecetasUsr/", addRecetasUsr),
    path("recetasUsr/", vista_recetasUsr),
    path("recetasMain/", vista_recetasMain),
    path("usuarios/", vista_usuario),



]