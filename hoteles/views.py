from django.shortcuts import render
from .models import Hotele, hotel_banners
# Create your views here.
def hoteles(request):
    hoteles = Hotele.objects.all()
    banners = hotel_banners.objects.all()
    return render(request, "hoteles/hoteles.html", {'hoteles': hoteles,'banners':banners})

def hoteles_details(request, pk):
    hotel = Hotele.objects.get(pk=pk)
    return render(request, "hoteles/hotelesdetails.html", {'hotel': hotel})