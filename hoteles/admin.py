from django.contrib import admin
from .models import Hotele
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')


admin.site.register(Hotele, ProjectAdmin)