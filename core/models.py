from django.db import models

# Create your models here.
class home_banner(models.Model):
    descripción = models.TextField()
    imagen = models.ImageField(verbose_name="Imagen", upload_to="home/banners")
    creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    class Meta:
        verbose_name = 'home_banners'
        verbose_name_plural = 'home_banners'
        ordering = ['-creacion'] 

    def __str__(self):
        return self.descripción