from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from products.models import Product
# Views


def view_cart(request):
    """ Renders the Shopping Cart page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Adds specified quantity of product to cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Added {quantity} for a total of \
                                    {cart[item_id]} {product.name}.')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {quantity} \
                                    {product.name}(s) to cart.')

    request.session['cart'] = cart
    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """
    Remove product from cart
    """
    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    cart.pop(item_id)
    messages.success(request, f'Removed {product.name} from cart.')
    request.session['cart'] = cart
    return redirect(redirect_url)


def update_quantity(request, item_id):
    """
    Updates the quantity of the specified product
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    cart[item_id] = quantity
    messages.success(request, f'Added {quantity} for a total of {cart[item_id]} \
                                {product.name}.')
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
