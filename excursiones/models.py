from django.db import models

# Create your models here.
class excursiones(models.Model):
    nombre_excursion = models.CharField(max_length=50)
    destino = models.CharField(max_length=50)
    salida = models.CharField(max_length=50)
    itinerario = models.CharField(max_length=50)
    capacidad_maxima = models.IntegerField()
    costo = models.DecimalField(decimal_places=3, max_digits=6)
    imagen = models.ImageField(verbose_name="Imagen", upload_to="excursiones")
    creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    class Meta:
        verbose_name = 'Excursiones'
        verbose_name_plural = 'Excursiones'
        ordering = ['-creacion'] 

    def __str__(self):
        return self.nombre_excursion
