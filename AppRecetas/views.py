from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from AppRecetas.forms import Form_AddRecetasMain



# Create your views here.

def inicio(request):
    return render(request,'AppRecetas/inicio.html')


def addRecetasMain(request):
  if request.method == "POST":#despues de dar click a eviar
    
    formulario1 = Form_AddRecetasMain(request.POST)
    
    if formulario1.is_valid():

      info =formulario1.cleaned_data

      res_Main = RecetasMain(nom_platos=info["nom_platos"],
                           ingredientes=request.POST["ingredientes"],
                           receta=request.POST["receta"],
                           tiempo=request.POST["tiempo"],
                           dificultad=request.POST["dificultad"],
                           tipoDeCocina=request.POST["tipoDeCocina"],
                           fuente=request.POST["fuente"], 
                           procedimiento=request.POST["procedimiento"])
      
      res_Main.save()                       
      return render(request,'AppRecetas/inicio.html')  
    
  else:
    formulario1 = Form_AddRecetasMain()

                         

  return render(request,'AppRecetas/addRecetasMain.html', {"form1" :formulario1})
  
                           


def addRecetasUsr(request):
  return render(request,'AppRecetas/addRecetasUsr.html')





def vista_recetasUsr(request):
  return render(request,'AppRecetas/recetasUsr.html')

def vista_recetasMain(request):
  return render(request,'AppRecetas/recetasMain.html')


def vista_usuario(request):

  return render(request,'AppRecetas/usuario.html')


def add_RecetasMain(request):

  return render(request, "AddrecetasMain")




