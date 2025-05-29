from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
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
            # Get form data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            
            # Prepare email content
            subject = f'New Contact Form Submission from {first_name} {last_name}'
            message = f'''
            New contact form submission:
            
            Name: {first_name} {last_name}
            Email: {email}
            Phone: {phone}
            
            Please respond to this inquiry as soon as possible.
            '''
            
            # Send email
            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.EMAIL_HOST_USER],  # Send to yourself
                    fail_silently=False,
                )
                messages.success(request, 'Thank you for your interest! We will contact you soon.')
                form = ContactForm()  # Reset form after successful submission
            except Exception as e:
                messages.error(request, 'There was an error sending your message. Please try again later.')
    else:
        form = ContactForm()
    
    return render(request, 'main/contact.html', {'form': form})
