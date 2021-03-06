from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class excursiones(models.Model):
    nombre_excursion = models.CharField(max_length=50)
    destino = models.CharField(max_length=50)
    salida = models.CharField(max_length=50)
    itinerario = RichTextField()
    capacidad_maxima = models.IntegerField()
    costo = models.CharField(max_length=50)
    imagen = models.ImageField(verbose_name="Imagen", upload_to="excursiones")
    recomendado = models.BooleanField(default=False)
    creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")
    
    class Meta:
        verbose_name = 'Excursiones'
        verbose_name_plural = 'Excursiones'
        ordering = ['-creacion'] 

    def __str__(self):
        return self.nombre_excursion

class excursion_banners(models.Model):
    descripción = models.TextField()
    imagen = models.ImageField(verbose_name="Imagen", upload_to="excursiones/banners")
    creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")
    
    class Meta:
        verbose_name = 'excursion_banners'
        verbose_name_plural = 'excursion_banners'
        ordering = ['-creacion'] 

    def __str__(self):
        return self.descripción

class imagenes(models.Model):
    property = models.ForeignKey(excursiones, related_name='images', on_delete=models.PROTECT)
    image = models.ImageField()

    class Meta:
        verbose_name = 'imagen'
        verbose_name_plural = 'Slider detalle'