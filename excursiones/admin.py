from django.contrib import admin
from .models import excursiones, excursion_banners, imagenes
# Register your models here.
class PropertyImageInline(admin.TabularInline):
    model = imagenes
    
class ExcursionesAdmin(admin.ModelAdmin):
    inlines = [ PropertyImageInline, ]
    readonly_fields = ('creacion', 'actualizacion')

admin.site.register(excursiones, ExcursionesAdmin)
admin.site.register(excursion_banners)