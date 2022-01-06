from django import forms

class ContactForm(forms.Form):
    nom = forms.CharField(required = False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)
