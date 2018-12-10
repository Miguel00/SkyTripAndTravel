from django.contrib import admin
from .models import tour, tour_banner, imagenes
# Register your models here.

class PropertyImageInline(admin.TabularInline):
    model = imagenes
    
class ToursAdmin(admin.ModelAdmin):
    inlines = [ PropertyImageInline, ]
    readonly_fields = ('creacion', 'actualizacion')

admin.site.register(tour, ToursAdmin)
admin.site.register(tour_banner)