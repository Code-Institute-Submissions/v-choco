from django.conf import settings


def cart_contents(request):

    cart_items = []
    order_total = 0
    product_count = 0

    if order_total < settings.FREE_SHIPPING_THRESHOLD:
        shipping = settings.STANDARD_SHIPPING_COST
        free_shipping_delta = settings.FREE_SHIPPING_THRESHOLD - order_total
    else:
        shipping = 0
        free_shipping_delta = 0

    grand_total = shipping + order_total

    context = {
        'cart_items': cart_items,
        'order_total': order_total,
        'product_count': product_count,
        'shipping': shipping,
        'free_shipping_delta': free_shipping_delta,
        'free_shipping_threshold': settings.FREE_SHIPPING_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
