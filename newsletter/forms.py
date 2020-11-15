from django import forms
from .models import NewsletterUser


class NewsletterSignupForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "type": "email",
        "name": "email",
        "id": "email",
        "placeholder": "Please enter your email.",
    }), label="")

    class Meta:
        model = NewsletterUser
        fields = ('email', )
