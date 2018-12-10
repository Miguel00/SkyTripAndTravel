from django.shortcuts import render, redirect
from django.urls import reverse
from .models import contacto_banner
from .forms import ContactForm
from django.core.mail import EmailMessage
# Create your views here.
def contacto(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            asunto = request.POST.get('asunto', '')
            content = request.POST.get('content', '')
            #enviar correo y redireccinar
            email = EmailMessage(
                'Skytrips&travel',
                'Asunto: {}\nDe {} <{}>\n\nEscribio:\n\n{}'.format(asunto, name, email, content),
                'no-contestar@inbox.mailtrap.io',
                ['esstrad4@gmail.com'],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact')+'?ok')
            except:
                return redirect(reverse('contact')+'?fail')

    contacto_banners = contacto_banner.objects.all()
    return render(request, "contacto/contact.html", {'contacto_banners': contacto_banners, 'form':contact_form})