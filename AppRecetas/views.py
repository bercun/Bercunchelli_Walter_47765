from django.shortcuts import render
from django.http import HttpResponse
from AppRecetas.models import RecetasMain, RecetasUsr, Usuario 
from AppRecetas.forms import Form_AddRecetasMain, FormAddRecetasUsr , FormAddUsuario


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
  
  if request.method == "POST":#despues de dar click a eviar
    
    formulario2 = FormAddRecetasUsr(request.POST)
    
    if formulario2.is_valid():

      info = formulario2.cleaned_data

      res_Usr = RecetasUsr(nom_platosUsr=info["nom_platosUsr"],
                           ingredientesUsr=info["ingredientesUsr"],
                           recetaUsr=info["recetaUsr"],
                           tiempoUsr=info["tiempoUsr"],
                           dificultadUsr=info["dificultadUsr"],
                           tipoDeCocinaUsr=info["tipoDeCocinaUsr"],
                           fuenteUsr=info["fuenteUsr"], 
                           procedimientoUsr=info["procedimientoUsr"])
      
      res_Usr.save()                       
      return render(request,'AppRecetas/inicio.html')  
    
  else:
    formulario2 = FormAddRecetasUsr()

                         

  return render(request,'AppRecetas/addRecetasUsr.html', {"form2" :formulario2})
  
                           

def addUsuario(request):
  if request.method == "POST":#despues de dar click a eviar
    
    formulario3 = FormAddUsuario(request.POST)
    
    if formulario3.is_valid():

      info = formulario3.cleaned_data

      addUsr = Usuario(nombreUsr=info["nombreUsr"],
                      emailUsr= info["emailUsr"],
                      telfonoUsr=info["telfonoUsr"],
                      ciudad=info["ciudad"],
                      edad =info["edad"],
      )
      addUsr.save()  
      
      return render(request,'AppRecetas/inicio.html')  
  else:
    formulario3 = FormAddUsuario()


  return render(request, "AppRecetas/addUsr.html", {"form3" : formulario3} )




def seekRecetas(request):

  return render(request, "AppRecetas/seekRecetas.html")


  

def showRecetas(request):

  if request.GET["ingredientes"]:

    ingreseek = request.GET["ingredientes"]
    recetasfind = RecetasMain.objects.filter(ingredientes__icontains=ingreseek)

   
    return render(request,"AppRecetas/showRecetas.html", {"ingreseek":ingreseek, "ingrefind": recetasfind })

  else:
   respuesta ="No enviaste datos"  
   return HttpResponse(respuesta)









def vista_recetasUsr(request):
  return render(request,'AppRecetas/recetasUsr.html')

def vista_recetasMain(request):
  return render(request,'AppRecetas/recetasMain.html')


def vista_usuario(request):

  return render(request,'AppRecetas/usuario.html')







