from django.shortcuts import render

from .models import contacto_banner
# Create your views here.
def contacto(request):
    contacto_banners = contacto_banner.objects.all()
    return render(request, "contacto/contact.html", {'contacto_banners': contacto_banners})