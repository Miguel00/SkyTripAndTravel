from django.contrib import admin
from .models import comentario, nosotros_banner
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')


admin.site.register(comentario, ProjectAdmin)
admin.site.register(nosotros_banner)