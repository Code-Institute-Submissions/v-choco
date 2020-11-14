from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, Category
from .forms import ProductForm


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
                                         " looking for."))
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


@login_required
def add_product(request):
    """ Creates a new product """
    if not request.user.is_superuser:
        messages.error(request, 'This function is only possible for admins.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Added new product')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, ("Failed to add the new product,"
                                     " please try again later."))
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
        'add_product': True,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edits an existing product """
    if not request.user.is_superuser:
        messages.error(request, 'This function is only possible for admins.')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'{product.name} has been updated!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, ("Failed to update product,"
                                     " please try again later."))
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Deletes a product from the database """
    if not request.user.is_superuser:
        messages.error(request, 'This function is only possible for admins.')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
