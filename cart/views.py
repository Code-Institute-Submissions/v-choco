from django.shortcuts import render

# Create your views here.

def view_cart(request):
    """ Renders the Shopping Cart page """

    return render(request, 'cart/cart.html')
