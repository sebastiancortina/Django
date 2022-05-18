from django.db import models

# Create your models here.
class Inmueble(models.Model):
    direccion = models.CharField(max_length=250)  #Almacena Texto
    pais = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=500)
    image = models.CharField(max_length=900)
    active = models.BooleanField(default=True)

    #Indicamos la columna que se desplegara en el panel de administracion de django
    def __str__(self):
        return self.direccion

