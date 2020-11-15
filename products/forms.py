from django import forms
from .models import Product, Category, ProductReview
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=True, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(cat.id,
                          cat.get_friendly_name()) for cat in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'input-field'


class ProductReviewForm(forms.ModelForm):
    content = forms.CharField(max_length=200,
                              label="",
                              required=False,
                              widget=forms.Textarea)
    CHOICES = (
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            )
    rating = forms.ChoiceField(widget=forms.Select,
                               choices=CHOICES,
                               initial='3')

    class Meta:
        model = ProductReview
        fields = ('rating', 'content', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'input-field'
