from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs = {'type':"text", 'class':"form-control", 'placeholder':"Nombre"}
    ))
    email = forms.EmailField(label="Correo", required=True, widget=forms.EmailInput(
        attrs = {'type':"email", 'class':"form-control", 'placeholder':"Correo"}
    ))
    asunto = forms.CharField(label="Asunto", required=True, widget=forms.TextInput(
        attrs = {'type':"text", 'class':"form-control", 'placeholder':"Asunto"}
    ))
    content = forms.CharField(label="Mensaje", required=True, widget=forms.Textarea(
        attrs = {'type':"text", 'class':"form-control", 'placeholder':"Mensaje"}
    ))