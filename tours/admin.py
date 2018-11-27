from django.contrib import admin
from .models import tour, tour_banner
# Register your models here.
class ToursAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')

admin.site.register(tour, ToursAdmin)
admin.site.register(tour_banner)