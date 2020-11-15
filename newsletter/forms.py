from django import forms
from .models import NewsletterUser


class NewsletterSignupForm(forms.ModelForm):
    class Meta:
        model = NewsletterUser
        fields = ('email', )
