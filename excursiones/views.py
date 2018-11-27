from django.shortcuts import render
from .models import excursiones 
# Create your views here.

def Excursiones(request):
    excursiones_all = excursiones.objects.all()
    return render(request, 'excursiones/servicios.html', {'excursiones':excursiones_all})
