from django.shortcuts import render
from .models import excursiones, excursion_banners
# Create your views here.

def Excursiones(request):
    excursiones_all = excursiones.objects.all()
    excursiones_banners = excursion_banners.objects.all()
    return render(request, 'excursiones/servicios.html', {'excursiones':excursiones_all, 'banners':excursiones_banners})
