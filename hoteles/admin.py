from django.contrib import admin
from .models import Hotele, hotel_banners, imagenes
# Register your models here.
class PropertyImageInline(admin.TabularInline):
    model = imagenes

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ PropertyImageInline, ]
    readonly_fields = ('creacion', 'actualizacion')


admin.site.register(Hotele, ProjectAdmin)
admin.site.register(hotel_banners)