from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import NewsletterSignupForm
from .models import NewsletterUser

import requests
import json

MAILCHIMP_API_KEY = settings.MAILCHIMP_API_KEY
MAILCHIMP_DATA_CENTER = settings.MAILCHIMP_DATA_CENTER
MAILCHIMP_EMAIL_LIST_ID = settings.MAILCHIMP_EMAIL_LIST_ID

api_url = f'https://{MAILCHIMP_DATA_CENTER}.api.mailchimp.com/3.0/'
members_endpoint = f'{api_url}/lists/{MAILCHIMP_EMAIL_LIST_ID}/members'


def subscribe(email):
    """ Saves new email addresses """
    data = {
        "email_address": email,
        "status": "subscribed"
    }
    r = requests.post(
        members_endpoint,
        auth=("", MAILCHIMP_API_KEY),
        data=json.dumps(data)
    )
    return r.status_code, r.json()


def newsletter_signup(request):
    """
    Checks whether email already exists
    in database. If not it will add the
    new email.
    """
    form = NewsletterSignupForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            newsletter_signup_query = NewsletterUser.objects.filter(email=form.instance.email)
            if newsletter_signup_query.exists():
                messages.error(request, "You are already subscribed!")
            else:
                subscribe(form.instance.email)
                form.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
