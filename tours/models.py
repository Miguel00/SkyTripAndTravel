from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class tour(models.Model):
    nombre_tour = models.CharField(max_length=50)
    pickup = models.CharField(max_length=50)
    duracion = models.CharField(max_length=50)
    costo = models.CharField(max_length=50)
    descripción = RichTextField()
    comentario = RichTextField()
    imagen = models.ImageField(verbose_name="Imagen", upload_to="tours")
    recomendado = models.BooleanField(default=False)
    creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    class Meta:
        verbose_name = 'Tours'
        verbose_name_plural = 'Tours'
        ordering = ['-creacion'] 

    def __str__(self):
        return self.nombre_tour

class tour_banner(models.Model):
    descripción = models.TextField()
    imagen = models.ImageField(verbose_name="Imagen", upload_to="tours/banners")
    creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    class Meta:
        verbose_name = 'tour_banners'
        verbose_name_plural = 'tour_banners'
        ordering = ['-creacion'] 

    def __str__(self):
        return self.descripción

class imagenes(models.Model):
    property = models.ForeignKey(tour, related_name='images', on_delete=models.PROTECT)
    image = models.ImageField()

    class Meta:
        verbose_name = 'imagen'
        verbose_name_plural = 'Slider detalle'


