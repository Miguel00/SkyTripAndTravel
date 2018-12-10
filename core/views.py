from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from hoteles.models import Hotele
from tours.models import tour
from excursiones.models import excursiones
from .models import home_banner
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def home(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            email = request.POST.get('email', '')
            #enviar correo y redireccinar
            email = EmailMessage(
                'SkyTrips&Travel',
                'Asunto: Newsletter\nCorreo: <{}>'.format(email),
                'no-contestar@inbox.mailtrap.io',
                ['esstrad4@gmail.com'],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('home')+'?ok')
            except:
                return redirect(reverse('home')+'?fail')

    hoteles = Hotele.objects.all()
    tours = tour.objects.all()
    home_banners = home_banner.objects.all()
    excursion =  excursiones.objects.all()
    return render(request, "core/home.html", {'hoteles': hoteles, 'tours':tours, 'home_banners':home_banners, 'excursiones':excursion, 'form':contact_form})
    
def about(request):
    return render(request, "core/about.html")

def contact(request):
    return render(request, "core/contact.html")

def destinos(request):
    return render(request, "core/terminos.html")

def politicas(request):
    return render(request, "core/politicas.html")

def tours(request):
    return render(request, "core/tours.html") 
