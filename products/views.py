from django.shortcuts import render
from .models import Product

# Create your views here.

def products(request):
    """ Renders all products ability to search and sort"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
