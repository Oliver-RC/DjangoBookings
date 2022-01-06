from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import NewsletterSignUp


def sign_up(request):
    form = NewsletterSignUp()
    if request.method == 'POST':
        form = NewsletterSignUp(request.POST)
        if form.is_valid():
            subject = "Arthur & Alfie's Newsletter Sign Up"
            message = 'Thank You for signing up to our montly newsletter. Sign Up Successful.'
            recipient = form.cleaned_data.get('email')
            send_mail(subject, 
              message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            messages.success(request, 'Success!')
            return redirect('sign_up')
    return render(request, 'newsletter.html', {'form': form})