from django.shortcuts import render

from .models import comentario, nosotros_banner
# Create your views here.
def about(request):
    comentario_feedback = comentario.objects.all()
    nosotros_banners = nosotros_banner.objects.all()
    return render(request, "nosotros/about.html", {'comentarios': comentario_feedback,'nosotros_banners':nosotros_banners})
