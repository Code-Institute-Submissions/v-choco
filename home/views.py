from django.shortcuts import render
from newsletter.forms import NewsletterSignupForm

# Views


def index(request):
    """ Renders the Index page """
    form = NewsletterSignupForm()

    context = {
        'form': form,
    }

    return render(request, 'home/index.html', context)
