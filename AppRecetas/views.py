from django.shortcuts import render
from django.http import HttpResponse
from AppRecetas.models import *


# Create your views here.

def recetasMain(request):

    receta_1 = RecetasMain(nom_platos= "pizza",
     ingredientes= "harina, agua, levadura, sal, aceite , salsa de tomate",
      receta= "harina 1kg, agua 0.5 litros, sal 10gr, levadura 10gr, sal 35, aceite 10cc",
      tiempo= 30, 
      dificultad= "media",
      tipoDeCocina= "una hora",
      fuente= "bercun",
      procedimiento=" mezclar el harina con el agua, agregar levadura, amasar, agregar la sal, agregar el aceite, dejar leudar por media hora(en zona con humedad y calor suave) colocar en bandeja de horo, agregar la salsa de tomante y cocinar en horno medio"
      )
    receta_1.save()

    return HttpResponse(f" La receta de {receta_1.nom_platos} \n es de dificultad {receta_1.dificultad} \n y los pasos de su elavoracion son {receta_1.procedimiento} ")  



