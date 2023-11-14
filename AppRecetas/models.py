from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RecetasMain(models.Model):


    def __str__(self):
        return f"  {self.nom_platos} -- Tipo de cocina: {self.tipoDeCocina} " 
    
    
    nom_platos = models.CharField(max_length=20)
    ingredientes = models.CharField(max_length=100)
    receta = models.CharField(max_length=100)
    tiempo = models.IntegerField()
    dificultad = models.CharField(max_length=10)
    tipoDeCocina = models.CharField(max_length=20)
    fuente = models.CharField(max_length=30)
    procedimiento = models.TextField()
    
class RecetasUsr(models.Model):

    def __str__(self):
        return f"  {self.nom_platosUsr} -- Tipo de cocina: {self.tipoDeCocinaUsr} " 
    
    nom_platosUsr = models.CharField(max_length=20)
    ingredientesUsr = models.CharField(max_length=100)
    recetaUsr = models.CharField(max_length=100)
    tiempoUsr = models.IntegerField()
    dificultadUsr = models.CharField(max_length=10)
    tipoDeCocinaUsr = models.CharField(max_length=20)
    fuenteUsr = models.CharField(max_length=30)
    procedimientoUsr = models.TextField()

class Cheff(models.Model):

    def __str__(self):
        return f"  {self.nombreUsr} -- Origen : {self.ciudad} " 
    
    nombreUsr = models.CharField(max_length=20)
    emailUsr = models.EmailField()
    telfonoUsr = models.IntegerField()
    ciudad = models.CharField(max_length=20)
    edad = models.IntegerField()
    tipoDeCocina = models.CharField(max_length=20)

class Avatar(models.Model):
    
    def __str__(self):
        return f"  {self.usuario} -- Avatar: {self.image} " 


    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to= "avatares", null=True, blank=True)



