from django.shortcuts import render, HttpResponse
from hoteles.models import Hotele
from tours.models import tours
# Create your views here.
def home(request):
    hoteles = Hotele.objects.all()
    tours = tours.objects.all()
    return render(request, "core/home.html", {'hoteles': hoteles, 'tours':tours})
    
def about(request):
    return render(request, "core/about.html")

def contact(request):
    return render(request, "core/contact.html")

def destinos(request):
    return render(request, "core/destinos.html")

def tours(request):
    return render(request, "core/tours.html") 
