from django import forms
from .models import NewsletterUser


class NewsletterSignUpForm(forms.ModelForm):

    class Meta:
        model = NewsletterUser
        fields = ('full_name', 'last_name', 'email',)

        def clean_email(self):
            email = self.cleaned_data.get('email')

            return email
