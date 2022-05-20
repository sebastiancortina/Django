from django.db import models

# Create your models here

class Empresa(models.Model):
    nombre = models.CharField(max_length=250)
    website = models.URLField(max_length=250)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Edificacion(models.Model):
    direccion = models.CharField(max_length=250)  #Almacena Texto
    pais = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=500)
    image = models.CharField(max_length=900)
    active = models.BooleanField(default=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="edificacion")
    created = models.DateTimeField(auto_now_add=True)
   

    #Indicamos la columna que se desplegara en el panel de administracion de django
    def __str__(self):
        return self.direccion

