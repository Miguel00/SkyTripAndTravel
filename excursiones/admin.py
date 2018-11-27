from django.contrib import admin
from .models import excursiones
# Register your models here.
class ExcursionesAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')

admin.site.register(excursiones, ExcursionesAdmin)