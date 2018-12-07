from django.contrib import admin
from .models import home_banner
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')


admin.site.register(home_banner, ProjectAdmin)
# admin.site.register(hotel_banners)