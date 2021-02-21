from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.http import HttpResponse
from .forms import ContactForm


def contact(request):
    """
    A view to return contact page and render the form
    """
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            subject = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['message']
            try:
                send_mail(
                    # to capture the user email it's displayd
                    # in subject field and can be responded to
                    f"Message from {name}, subject: '{subject}'",
                    message,
                    email,
                    [settings.DEFAULT_FROM_EMAIL],

                )

                messages.success(request, f'Your message has been\
                                           successfully sent. Thank\
                                           you! We will answer\
                                           within 3 days!')
                return redirect('contact')

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    else:
        contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
        'from_event': True,
    }

    return render(request, 'contact/contact.html', context)
