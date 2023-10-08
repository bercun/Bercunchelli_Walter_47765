from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User





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




class FormAddUsuario(forms.Form):
    
    nombreUsr = forms.CharField(max_length=20)
    emailUsr = forms.EmailField()
    telfonoUsr = forms.IntegerField()
    ciudad = forms.CharField(max_length=20)
    edad = forms.IntegerField()

    
class FormAddUsuario(forms.Form):
    
    nombreUsr = forms.CharField(max_length=20)
    emailUsr = forms.EmailField()
    telfonoUsr = forms.IntegerField()
    ciudad = forms.CharField(max_length=20)
    edad = forms.IntegerField()

"""
class UserRegiser(UserCreationForm):

    email = forms.EmailField()
    nombre = forms.CharField()
    passw1 = forms.CharField(label= "contraseña", widget=forms.PasswordInput)
    passw2 = forms.CharField(label= "reiterar la contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields= ["username", "email", "fist_name", "password1", "password2"]

"""
    


