from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView
from .models import Service, StoneType
from .forms import ContactForm

def home(request):
    services = Service.objects.all()[:6]
    stone_types = StoneType.objects.all()[:6]
    
    context = {
        'services': services,
        'stone_types': stone_types,
    }
    return render(request, 'company/home.html', context)

def about(request):
    return render(request, 'company/about.html')

def services(request):
    services = Service.objects.all()
    return render(request, 'company/services.html', {'services': services})

def stone_types(request):
    stone_types = StoneType.objects.all()
    return render(request, 'company/stone_types.html', {'stone_types': stone_types})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your inquiry! We will contact you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'company/contact.html', {'form': form})