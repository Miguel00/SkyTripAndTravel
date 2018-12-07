from django.shortcuts import render, HttpResponse
from hoteles.models import Hotele
from tours.models import tour
from excursiones.models import excursiones
from .models import home_banner
# Create your views here.
def home(request):
    hoteles = Hotele.objects.all()
    tours = tour.objects.all()
    home_banners = home_banner.objects.all()
    excursion =  excursiones.objects.all()
    return render(request, "core/home.html", {'hoteles': hoteles, 'tours':tours, 'home_banners':home_banners, 'excursiones':excursion})
    
def about(request):
    return render(request, "core/about.html")

def contact(request):
    return render(request, "core/contact.html")

def destinos(request):
    return render(request, "core/destinos.html")

def tours(request):
    return render(request, "core/tours.html") 
