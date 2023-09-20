from django.db import models

# Create your models here.
class RecetasMain(models.Model):
    
    nom_platos = models.CharField(max_length=20)
    ingredientes = models.CharField(max_length=100)
    receta = models.CharField(max_length=100)
    tiempo = models.IntegerField()
    dificultad = models.CharField(max_length=10)
    tipoDeCocina = models.CharField(max_length=20)
    fuente = models.CharField(max_length=30)
    procedimiento = models.TextField()
    
class RecetasUsr(models.Model):
    
    nom_platosUsr = models.CharField(max_length=20)
    ingredientesUsr = models.CharField(max_length=100)
    recetaUsr = models.CharField(max_length=100)
    tiempoUsr = models.IntegerField()
    dificultadUsr = models.CharField(max_length=10)
    tipoDeCocinaUsr = models.CharField(max_length=20)
    fuenteUsr = models.CharField(max_length=30)
    procedimientoUsr = models.TextField()

class Usuario(models.Model):
    
    nombreUsr = models.CharField(max_length=20)
    emailUsr = models.EmailField()
    telfonoUsr = models.IntegerField()
    ciudad = models.CharField(max_length=20)
    edad = models.IntegerField()