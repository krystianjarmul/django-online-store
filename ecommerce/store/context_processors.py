from .models import Order

def products_in_cart(request):
    customer = request.user.customer
    order = customer.order_set.first()
    return {'products_in_cart': order}