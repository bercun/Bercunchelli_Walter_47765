from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppRecetas.models import Avatar





class Form_AddRecetasMain(forms.Form):
    nom_platos = forms.CharField(max_length=20)
    ingredientes = forms.CharField(max_length=100)
    receta = forms.CharField(max_length=100)
    tiempo = forms.IntegerField()
    dificultad = forms.CharField(max_length=10)
    tipoDeCocina = forms.CharField(max_length=20)
    fuente = forms.CharField(max_length=30)
    procedimiento = forms.CharField()
    

class FormAddRecetasUsr(forms.Form):
    
    nom_platosUsr = forms.CharField(max_length=20)
    ingredientesUsr = forms.CharField(max_length=100)
    recetaUsr = forms.CharField(max_length=100)
    tiempoUsr = forms.IntegerField()
    dificultadUsr = forms.CharField(max_length=10)
    tipoDeCocinaUsr = forms.CharField(max_length=20)
    fuenteUsr = forms.CharField(max_length=30)
    procedimientoUsr = forms.CharField()




class FormAddCheff(forms.Form):
    
    nombreUsr = forms.CharField(max_length=20)
    emailUsr = forms.EmailField()
    telfonoUsr = forms.IntegerField()
    ciudad = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    tipoDeCocina = forms.CharField()
"""   
class FormAddUsuario(forms.Form):
    
    nombreUsr = forms.CharField(max_length=20)
    emailUsr = forms.EmailField()
    telfonoUsr = forms.IntegerField()
    ciudad = forms.CharField(max_length=20)
    edad = forms.IntegerField()
"""

class UserRegiser(UserCreationForm):

    email = forms.EmailField()
    

    class Meta:

        model = User
        fields= ["username","first_name", "email",  "password1", "password2"]


class EditUsrForm(UserCreationForm):

    mail = forms.EmailField()
    

    class Meta:

        model = User
        fields= ["first_name", "email",  "password1", "password2"]





class AvatarForm(forms.ModelForm):

    class Meta:
        model=Avatar
        fields= [ "image"]
    
    
        



