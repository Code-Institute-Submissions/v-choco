from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def products(request):
    """ Renders all products and ability to search and sort"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

def product_details(request, product_id):
    """ Renders product details on a specific product"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)
