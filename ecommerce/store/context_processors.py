from store.models import OrderItem, Product, Order


def products_in_cart(request):
    if not request.user.is_authenticated:
        cart = request.session.get('cart', {})
        items = [OrderItem(product=Product.objects.get(pk=int(id)),
                           quantity=quantity) for id, quantity in cart.items()]
        cart_items = sum([item.quantity for item in items])

        return {'products_in_cart': cart_items}

    customer = request.user.customer

    order, created = Order.objects.get_or_create(customer=customer,
                                                 complete=False)


    return {'products_in_cart': order.get_cart_items}