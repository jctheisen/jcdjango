from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import redirect

from django.shortcuts import render
from listings.models import Groupe
from listings.forms import ContactForm


# Create your views here.

def hello(request):
    return HttpResponse('<h1>welcome django</h1>')

def groupes_liste(request):
    groupe = Groupe.objects.all()
    return render(request, 'listings/groupe_liste.html', {'igroupe': groupe})

def groupe_detail(request, xid):
    groupe = Groupe.objects.get(id=xid)
    return render(request, 'listings/groupe_detail.html', {'groupe': groupe})

def contact(request):

  print('La méthode de requête est : ', request.method)
  print('Les données POST sont : ', request.POST)

  if request.method == 'POST':
      iform = ContactForm(request.POST)  
      if iform.is_valid():
            print('envoi mail avec fonction send_mail')
            send_mail(
            subject=f'Message from {iform.cleaned_data["nom"] or "anonyme"} via MerchEx Contact Us form',
            message=iform.cleaned_data['message'],
            from_email=iform.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
            )
            return redirect('email-envoye')
  else:
      iform = ContactForm()  
  return render(request,
          'listings/contact.html',
          {'form': iform})  

def confirm(request):
    return render(request, 'listings/confirm.html')