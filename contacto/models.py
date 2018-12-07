from django.db import models

# Create your models here.
class contacto_banner(models.Model):
    descripcion = models.TextField()
    imagen = models.ImageField(verbose_name="Imagen", upload_to="contacto/banners")
    creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    class Meta:
        verbose_name = 'contacto_banners'
        verbose_name_plural = 'contacto_banners'
        ordering = ['-creacion'] 

    def __str__(self):
        return self.descripcion