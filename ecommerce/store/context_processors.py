from .models import Order

def products_in_cart(request):
    if not request.user.is_authenticated:
        return {'products_in_cart': 0}

    customer = request.user.customer
    order = customer.order_set.first()

    return {'products_in_cart': order}