from django.shortcuts import render
from django.contrib import messages

from marketing.forms import NewsletterSignupForm
from marketing.models import NewsletterSignup

from products.models import ProductReview


def index(request):
    """
    Renders homepage and Newsletter Sign Up forms
    """
    form = NewsletterSignupForm()
    reviews = ProductReview.objects.all()
    if request.method == "POST":
        email = request.POST["email"]
        query = NewsletterSignup.objects.filter(email__iexact=email)
        if form.is_valid:
            if query.exists():
                messages.error(request, "You're already subscribed!")
            else:
                email = request.POST["email"]
                new_signup = NewsletterSignup()
                new_signup.email = email
                new_signup.save()
                messages.success(request, "Successfully subscribed")

    context = {
        'form': form,
        'home_page': True,
        'reviews': reviews,
    }
    return render(request, 'home/index.html', context)
