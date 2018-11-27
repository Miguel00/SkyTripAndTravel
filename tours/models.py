from django.db import models

# Create your models here.
class tour(models.Model):
    nombre_tour = models.CharField(max_length=50)
    pickup = models.CharField(max_length=50)
    duracion = models.CharField(max_length=50)
    costo = models.DecimalField(decimal_places=3, max_digits=6)
    descripción = models.TextField()
    comentario = models.TextField()
    imagen = models.ImageField(verbose_name="Imagen", upload_to="tours")
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