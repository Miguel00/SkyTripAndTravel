from django.contrib import admin
from .models import contacto_banner

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')


admin.site.register(contacto_banner, ProjectAdmin)