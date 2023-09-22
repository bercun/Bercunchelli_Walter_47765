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
    


    



