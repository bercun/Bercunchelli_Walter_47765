from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppRecetas.models import Avatar, DificultadChoices





class Form_AddRecetasMain(forms.Form):
    nom_platos = forms.CharField(max_length=20)
    ingredientes = forms.CharField(max_length=100,
        help_text="Ej: 2 kg harina, 3 unidad huevo, 200 ml leche")
    receta = forms.CharField(max_length=100)
    tiempo = forms.IntegerField()
    dificultad = forms.ChoiceField(choices=DificultadChoices.choices)
    tipoDeCocina = forms.CharField(max_length=20)
    fuente = forms.CharField(max_length=30)
    procedimiento = forms.CharField(widget=forms.Textarea,
        help_text="Tip: también puedes cargar pasos uno por línea abajo")
    imagen = forms.ImageField(required=False)
    

class FormAddRecetasUsr(forms.Form):
    
    nom_platosUsr = forms.CharField(max_length=20)
    ingredientesUsr = forms.CharField(max_length=100,
        help_text="Ej: 2 kg harina, 3 unidad huevo, 200 ml leche")
    recetaUsr = forms.CharField(max_length=100)
    tiempoUsr = forms.IntegerField()
    dificultadUsr = forms.ChoiceField(choices=DificultadChoices.choices)
    tipoDeCocinaUsr = forms.CharField(max_length=20)
    fuenteUsr = forms.CharField(max_length=30)
    procedimientoUsr = forms.CharField(widget=forms.Textarea,
        help_text="Tip: también puedes cargar pasos uno por línea abajo")
    imagenUsr = forms.ImageField(required=False)




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
    
    
        



