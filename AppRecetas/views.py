from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views.generic import ListView , FormView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView  

from django.contrib.auth.forms import AuthenticationForm ,UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

#Decorador por defecto
from django.contrib.auth.decorators import login_required

from AppRecetas.models import RecetasMain, RecetasUsr, Cheff , Avatar
from AppRecetas.forms import *




# Create your views here.

#authentications  

def inicioDeSesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usr = form.cleaned_data.get('username')
            pssw = form.cleaned_data.get('password')
            user = authenticate(username=usr, password=pssw)
            if user is not None:
                login(request, user)
                return render(request, 'AppRecetas/inicio.html', {'mensaje': f'login correcto {user}'})
            else:
                return render(request, 'AppRecetas/inicio.html', {'mensaje': 'login Erroneo'})
    else:
        form = AuthenticationForm()
    return render(request, "AppRecetas/login.html", {'formulario': form})


def register (request):

  if request.method == "POST":

    form = UserRegiser(request.POST)
    if form.is_valid():

      username = form.cleaned_data ["username"]
      form.save()
      return render(request, 'AppRecetas/inicio.html', {"mensaje": "Usuario creado"} )
  else:
    form = UserRegiser()

  return render(request, "AppRecetas/register.html", {'formulario': form})  

@login_required
def editarUsuario (request):

  usr  = request.user

  if request.method == "POST":

    form = EditUsrForm(request.POST)

    if form.is_valid():

      info = form.cleaned_data

      usr.email = info["email"]
      usr.set_password(info["password1"])
      usr.first_name = ["first_name"]

      usr.save()

      return render(request, "AppRecetas/inicio.html")

  else:

    form = EditUsrForm( initial={"email" : usr.email,
                                 "first_name": usr.first_name,})

  return render(request, "AppRecetas/editPerfil.html", {"formulario": form, "usuario": usr} )


@login_required
def addAvatar(request):
  if request.method=="POST":

    form=AvatarForm(request.POST, request.FILES)

    if form.is_valid():
      usuarioActual = User.objects.get(username=request.user)

      avatar = Avatar(usuario=usuarioActual, image=form.cleaned_data["image"])
      
      avatar.save()

      return render(request, "AppRecetas/inicio.html" )
  else:
    form =AvatarForm()

  return render(request, "AppRecetas/addAvatar.html", {"formulario" : form})  



def inicio(request):
    return render(request,'AppRecetas/inicio.html')

def about(request):
    return render(request,'AppRecetas/about.html')


def test(request):
  return render(request, "AppRecetas/base.html" )
# ingresar datos "C"UD 


@login_required
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
  
@login_required
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
                        
@login_required
def addCheff(request):
  if request.method == "POST":#despues de dar click a eviar
    
    formulario3 = FormAddCheff(request.POST)
    
    if formulario3.is_valid():

      info = formulario3.cleaned_data

      addUsr = Cheff(nombreUsr=info["nombreUsr"],
                      emailUsr= info["emailUsr"],
                      telfonoUsr=info["telfonoUsr"],
                      ciudad=info["ciudad"],
                      edad =info["edad"],
                      tipoDeCocina=info["tipoDeCocina"],
      )
      addUsr.save()  
      
      return render(request,'AppRecetas/inicio.html')  
  else:
    formulario3 = FormAddCheff()


  return render(request, "AppRecetas/addUsr.html", {"form3" : formulario3} )

#buscar y mostrar datos C"R"UD


def seekRecetas(request):

  return render(request, "AppRecetas/seekRecetas.html")

def showRecetas(request):

  if request.GET["ingredientes"]:

    ingreseek = request.GET["ingredientes"]
    recetasfind = RecetasMain.objects.filter(ingredientes__icontains=ingreseek)
    

    
    return render(request,"AppRecetas/showRecetas.html", {"ingreseek":ingreseek, "ingrefind": recetasfind ,  })

  else:
   respuesta ="No enviaste datos"  
   return HttpResponse(respuesta)                                 


def seekRecetasUsr(request):

  return render(request, "AppRecetas/seekRecetasUsr.html")


def showRecetasUsr(request):

  if request.GET["ingrediUsr"]:

    ingreseekUsr = request.GET["ingrediUsr"]
    recetasfindUsr = RecetasUsr.objects.filter(ingredientesUsr__icontains=ingreseekUsr)

    return render(request, "AppRecetas/showRecetasUsr.html", {"ingreBus" : ingreseekUsr, "recetasfoundUsr": recetasfindUsr})


  else:
   respuesta ="No enviaste datos"  
   return HttpResponse(respuesta)   


@login_required
def seekUsr(request):
  return render(request,"AppRecetas/seekUsr.html")

@login_required
def showUsr(request):

  if request.GET["Usr"]:

    ingreCeffseek = request.GET["Usr"]
    Cefffind = Cheff.objects.filter(nombreUsr__icontains=ingreCeffseek)
    

    
    return render(request,"AppRecetas/showUsr.html", {"ingreUsrseek":ingreCeffseek, "Usrfind": Cefffind })

  else:
   respuesta ="No enviaste datos"  
   return HttpResponse(respuesta)                                 



#modificar datos CR"U"D
@login_required
def update_RecetasMain(request, recetas):
  
  recetas_eli = RecetasMain.objects.get(nom_platos=recetas)

  if request.method == "POST":#despues de dar click a eviar
    
    formulario1 = Form_AddRecetasMain(request.POST)
    
    if formulario1.is_valid():

      info = formulario1.cleaned_data

      recetas_eli.nom_platos = info["nom_platos"]
      recetas_eli.tipoDeCocina = info["tipoDeCocina"]
      recetas_eli.ingredientes = info["ingredientes"]
      recetas_eli.receta = info["receta"]
      recetas_eli.tiempo = info["tiempo"]
      recetas_eli.dificultad = info["dificultad"]
      recetas_eli.fuente = info["fuente"]
      recetas_eli.procedimiento = info["procedimiento"]
      
      recetas_eli.save() 
      
      return render(request,'AppRecetas/inicio.html')  

  else:

    formulario1 = Form_AddRecetasMain(initial ={  "nom_platos" : recetas_eli.nom_platos,
                                                  "tipoDeCocina" : recetas_eli.tipoDeCocina,
                                                  "ingredientes" : recetas_eli.ingredientes,
                                                  "receta" : recetas_eli.receta,
                                                  "tiempo" : recetas_eli.tiempo,
                                                  "dificultad" : recetas_eli.dificultad,
                                                  "fuente" :recetas_eli.fuente,
                                                  "procedimiento" : recetas_eli.procedimiento} )
  
  return render(request, "AppRecetas/updateRecetasMain.html", {"formulario1": formulario1 , "recetas" : recetas  } )    

@login_required    
def update_RecetasUsr(request, recetasUsr):

  recetas_eli_Usr = RecetasUsr.objects.get(nom_platosUsr=recetasUsr)

  if request.method == "POST":#despues de dar click a eviar
    
    formulario2 = Form_AddRecetasUsr(request.POST)
    
    if formulario2.is_valid():

      info = formulario2.cleaned_data

      recetas_eli_Usr.nom_platosUsr = info["nom_platosUsr"]
      recetas_eli_Usr.tipoDeCocinaUsr = info["tipoDeCocinaUsr"]
      recetas_eli_Usr.ingredientesUsr = info["ingredientesUsr"]
      recetas_eli_Usr.recetaUsr = info["recetaUsr"]
      recetas_eli_Usr.tiempoUsr = info["tiempoUsr"]
      recetas_eli_Usr.dificultadUsr = info["dificultadUsr"]
      recetas_eli_Usr.fuenteUsr = info["fuenteUsr"]
      recetas_eli_Usr.procedimientoUsr = info["procedimientoUsr"]
      
      recetas_eli_Usr.save() 
      
      return render(request,'AppRecetas/inicio.html')  

  else:

    formulario2 = FormAddRecetasUsr(initial ={  "nom_platosUsr" : recetas_eli_Usr.nom_platosUsr,
                                                  "tipoDeCocinaUsr" : recetas_eli_Usr.tipoDeCocinaUsr,
                                                  "ingredientesUsr" : recetas_eli_Usr.ingredientesUsr,
                                                  "recetaUsr" : recetas_eli_Usr.recetaUsr,
                                                  "tiempoUsr" : recetas_eli_Usr.tiempoUsr,
                                                  "dificultadUsr" : recetas_eli_Usr.dificultadUsr,
                                                  "fuenteUsr" :recetas_eli_Usr.fuenteUsr,
                                                  "procedimientoUsr" : recetas_eli_Usr.procedimientoUsr} )
  
  return render(request, "AppRecetas/updateRecetasUsr.html", {"formulario2": formulario2 , "recetasUsr" : recetasUsr  } )    




#para listar, recetas totales y usuarios ****listas***

def vista_recetasMain(request):

  recetasUsr_all = RecetasUsr.objects.all()
  recetasMain_all = RecetasMain.objects.all()

    
  return render(request,'AppRecetas/recetasMain.html', {"lista_recetasUsr" : recetasUsr_all , "lista_recetasMain": recetasMain_all})




def vista_recetasUsr(request):
  
  
  return render(request,'AppRecetas/recetasMain.html')


@login_required
def vista_cheffs(request):
   cheff_all = Cheff.objects.all()
   listado = {"gente": cheff_all}

   return render(request, "AppRecetas/cheffs.html", listado )





#modificar datos CRU"D"    
@login_required
def eliminarRecetasUsr(request, nom_recetasUsr):
  recetasUsr_eli = RecetasUsr.objects.get(nom_platosUsr=nom_recetasUsr)
  recetasUsr_eli.delete()

  recetasUsr_remain = RecetasUsr.objects.all()

  envioWeb ={"lista_recetasUsr": recetasUsr_remain}

  return render(request, "AppRecetas/recetasMain.html", envioWeb)

@login_required
def eliminarRecetasMain(request, recetas):
  recetas_eli =RecetasMain.objects.get(nom_platos=recetas)
  recetas_eli.delete()

  
  recetas_remain = RecetasMain.objects.all()

  envWeb = {"lista_recetasMain": recetas_remain}

  return render(request, "AppRecetas/recetasMain.html", envWeb)


    # CRUD con clases

#Cheff

class ListaCheff(LoginRequiredMixin, ListView):

  model = Cheff

class DetalleCheff(LoginRequiredMixin, DetailView):
  
  model  = Cheff

class CrearCheff(LoginRequiredMixin, CreateView):
 
  model = Cheff
  success_url = "/AppRecetas/cheff/list"
  fields = ["nombreUsr","emailUsr","telfonoUsr","ciudad","edad", "tipoDeCocina"]

class UpdateCheff(LoginRequiredMixin, UpdateView):

  model = Cheff
  success_url = "/AppRecetas/cheff/list"
  fields = ["nombreUsr","emailUsr","telfonoUsr","ciudad","edad", "tipoDeCocina"]

class BorrarCheff(LoginRequiredMixin, DeleteView):
  model = Cheff  
  success_url = "/AppRecetas/cheff/list"     
    

#Avatar



class ListaAvatar(LoginRequiredMixin, ListView):

  model = Avatar

  def get_queryset(self):
        # Filtra los avatares del usuario logeado
        return Avatar.objects.filter(usuario=self.request.user)


  

