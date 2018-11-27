from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def contact(request):
    return render(request, "core/contact.html")

def destinos(request):
    return render(request, "core/destinos.html")

# def servicios(request):
#     return render(request, "core/servicios.html")

def tours(request):
    return render(request, "core/tours.html") 
