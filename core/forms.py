from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(label="Correo", required=True, widget=forms.EmailInput(
        attrs = {'type':"email", 'class':"form-control", 'placeholder':"Correo electrónico"}
    ))