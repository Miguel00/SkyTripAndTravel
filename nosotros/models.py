from django.db import models

# Create your models here.
class comentario(models.Model): 
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    lugar = models.CharField(max_length=50)

    creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")


    class Meta:
        verbose_name = 'Comentarios'
        verbose_name_plural = 'Comentarios'
        ordering = ['-creacion'] 

    def __str__(self):
        return self.nombre

class nosotros_banner(models.Model):
    descripcion = models.TextField()
    imagen = models.ImageField(verbose_name="Imagen", upload_to="nosotros/banners")
    creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    class Meta:
        verbose_name = 'nosotros_banners'
        verbose_name_plural = 'nosotros_banners'
        ordering = ['-creacion'] 

    def __str__(self):
        return self.descripcion