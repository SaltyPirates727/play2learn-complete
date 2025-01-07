from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings
from .forms import ContactForm

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Send email
            send_mail(
                f"Message from {form.cleaned_data['name']}",
                form.cleaned_data['message'],
                form.cleaned_data['email'],
                [settings.DEFAULT_FROM_EMAIL],  # Change this to the admin's email
                fail_silently=False,
            )
            return render(request, 'contact/contact_us.html', {'form': form, 'success': True})
    else:
        form = ContactForm()

    return render(request, 'contact/contact_us.html', {'form': form})
