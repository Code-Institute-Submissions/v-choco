from django import forms

from .models import NewsletterSignup


class NewsletterSignupForm(forms.ModelForm):
    email = forms.EmailField(label='',
                             widget=forms.EmailInput(
                                 attrs={'placeholder': 'Enter Your Email',
                                        'class': 'form-control'}
                                ))

    class Meta:
        model = NewsletterSignup
        fields = ('email', )
