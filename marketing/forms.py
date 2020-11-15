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

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        print(email)
        query = NewsletterSignup.objects.filter(email__iexact=email)
        if query.exists():
            raise forms.ValidationError("This email is already subscribed.")
        return email
