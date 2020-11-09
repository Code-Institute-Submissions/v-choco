from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


def products(request):
    """ Renders all products and ability to search and sort"""

    products = Product.objects.all()
    categories = Category.objects.all()
    query = None
    category = None

    if request.GET:
        if 'category' in request.GET:
            category = request.GET['category'].split()
            products = products.filter(category__name__in=category)
            category = Category.objects.filter(name__in=category)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, ("Please enter what you are"
                                         "looking for."))
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search': query,
        'categories': categories,
        'current_category': category,
    }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ Renders product details on a specific product"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)
