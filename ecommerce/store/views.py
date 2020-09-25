from django.shortcuts import render, redirect

from .models import Product, Order, OrderItem


def home(request):
    context = {}
    return render(request, 'store/main.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, craeted = Order.objects.get_or_create(customer=customer,
                                                     complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}

    context = {'items': items, 'order': order}
    return render(request, 'store/cart.html', context)

def store(request):
    products = Product.objects.all()
    context = {'products': products}

    return render(request, 'store/store.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,
                                                     complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}

    context = {'items': items, 'order': order}
    return render(request, 'store/checkout.html', context)

def update_cart(request, id):
    if not request.user.is_authenticated:
        return redirect('store')

    customer = request.user.customer
    order = customer.order_set.first()
    product = Product.objects.get(pk=id)

    if product.orderitem_set.first() not in order.orderitem_set.all():
        item = OrderItem(order=order, quantity=1, product=product)
        item.save()
    else:
        item = OrderItem.objects.get(order=order, product=product)
        item.quantity += 1
        item.save()

    return redirect('store')

def add_item(request, id):
    if not request.user.is_authenticated:
        return redirect('cart')

    customer = request.user.customer
    order = customer.order_set.first()
    product = Product.objects.get(pk=id)
    item = OrderItem.objects.get(order=order, product=product)
    item.quantity += 1
    item.save()

    return redirect('cart')

def remove_item(request, id):
    if not request.user.is_authenticated:
        return redirect('cart')

    customer = request.user.customer
    order = customer.order_set.first()
    product = Product.objects.get(pk=id)
    item = OrderItem.objects.get(order=order, product=product)
    item.quantity -= 1

    if item.quantity == 0:
        item.delete()
    else:
        item.save()

    return redirect('cart')



