from django.db import models

# Create your models here.
class Hotele(models.Model): 
    destino = models.CharField(max_length=50)
    nombre_hotel = models.CharField(max_length=50)
    capacidad_habitacion = models.IntegerField()
    costo = models.DecimalField(decimal_places=3, max_digits=6)
    descripción = models.TextField()
    imagen = models.ImageField(verbose_name="Imagen", upload_to="hoteles")
    creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    class Meta:
        verbose_name = 'Hoteles'
        verbose_name_plural = 'Hoteles'
        ordering = ['-creacion'] 

    def __str__(self):
        return self.nombre_hotel

class hotel_banners(models.Model):
    descripción = models.TextField()
    imagen = models.ImageField(verbose_name="Imagen", upload_to="hoteles/banners")
    creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    class Meta:
        verbose_name = 'hotel_banners'
        verbose_name_plural = 'hotel_banners'
        ordering = ['-creacion'] 

    def __str__(self):
        return self.descripción