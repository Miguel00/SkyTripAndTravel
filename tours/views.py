from django.shortcuts import render
from .models import tour, tour_banner
# Create your views here.

def tours(request):
    Tours = tour.objects.all()
    Tours_banners = tour_banner.objects.all()
    return render(request, "tours/tours.html", {"tours": Tours, "banners":Tours_banners }) 

def tours_details(request, pk):
    property = tour.objects.get(pk=pk)
    image_list = property.images.all()
    return render(request, "tours/toursdetails.html", {"tour": property,'slider':image_list}) 