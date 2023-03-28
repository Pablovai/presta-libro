from django.shortcuts import render, redirect
from .forms import HumoForm
from django.contrib import messages
from .models import ContactoPrincipal


def contacto_principal(request):
    if request.method == "POST":
        form = HumoForm(request.POST)
        if form.is_valid():
            data = ContactoPrincipal()
            data.first_name = form.cleaned_data['first_name']
            data.email = form.cleaned_data['email']
            data.coments = form.cleaned_data['coments']
            data.save()
            return redirect('contacto_principal')        
    else:
        form = HumoForm()

    return render(request, 'contacto/contacto_principal.html', {'form': form})





