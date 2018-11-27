from django.shortcuts import render
from .models import Hotele
# Create your views here.
def hoteles(request):
    hoteles = Hotele.objects.all()
    return render(request, "hoteles/hoteles.html", {'hoteles': hoteles})