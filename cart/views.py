from django.shortcuts import render, redirect, reverse
# Views


def view_cart(request):
    """ Renders the Shopping Cart page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Adds specified quantity of product to cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """
    Remove product from cart
    """
    cart = request.session.get('cart', {})
    cart.pop(item_id)
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def update_quantity(request, item_id):
    """
    Updates the quantity of the specified product
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    cart[item_id] = quantity
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
