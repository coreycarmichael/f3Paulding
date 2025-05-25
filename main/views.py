from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm

# Create your views here.

def home(request):
    return render(request, 'main/home.html')

def about_f3(request):
    return render(request, 'main/about_f3.html')

def paulding_region(request):
    return render(request, 'main/paulding_region.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Here you would typically send an email or save to database
            # For now, we'll just show a success message
            messages.success(request, 'Thank you for your interest! We will contact you soon.')
            form = ContactForm()  # Reset form after successful submission
    else:
        form = ContactForm()
    
    return render(request, 'main/contact.html', {'form': form})
