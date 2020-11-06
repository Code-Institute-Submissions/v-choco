from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart')
    if not cart:
        messages.error(request, "Your cart is empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HXtUSESZVPCI9L2w3toInYlUdFxUQxlagElJc135DDkCgAB59hDGc482ftZ71jwT8o7pgmIJ2oSDVnNGTySpY5500i6wB3bCc',
        'client_secret': 'test_client_secret',
    }

    return render(request, template, context)