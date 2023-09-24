from django import forms

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


