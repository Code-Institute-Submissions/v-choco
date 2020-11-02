from django.shortcuts import render

# Views


def view_cart(request):
    """ Renders the Shopping Cart page """

    return render(request, 'cart/cart.html')
