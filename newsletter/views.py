from django.shortcuts import render

from .models import NewsletterUser
from .forms import NewsletterSignUpForm


def newsletter_signup(request):
    form = NewsletterSignUpForm

    if request.method == 'POST':
        instance = form.save(commit=False)

        if NewsletterUser.objects.filter(email=instance.email).exists():
            print("sorry this email already exists")
        else:
            instance.save()

    template = "home/index.html"
    context = {
        'form': form,
    }

    return render(request, template, context)
