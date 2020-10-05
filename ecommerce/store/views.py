from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from .models import Product, Order, OrderItem
from ecommerce import settings


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

        if not request.session.get('cart'):
            request.session['cart'] = {}

        cart = request.session.get('cart', {})
        items = [OrderItem(product=Product.objects.get(pk=int(id)),
                           quantity=quantity) for id, quantity in cart.items()]
        cart_items = sum([int(item.quantity) for item in items])
        cart_total = sum([item.product.price * int(item.quantity) for item in items])

        order = {'get_cart_items': cart_items, 'get_cart_total': cart_total}

    context = {'items': items, 'order': order}

    return render(request, 'store/cart.html', context)


def store(request):
    products = Product.objects.all()

    paginator = Paginator(products, settings.PRODUCTS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'products': products, 'page_obj': page_obj}

    return render(request, 'store/store.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,
                                                     complete=False)
        items = order.orderitem_set.all()
    else:
        if not request.session.get('cart'):
            request.session['cart'] = {}

        cart = request.session.get('cart', {})
        items = [OrderItem(product=Product.objects.get(pk=int(id)),
                           quantity=quantity) for id, quantity in cart.items()]
        cart_items = sum([item.quantity for item in items])
        cart_total = sum([item.product.price * item.quantity for item in items])

        order = {'get_cart_items': cart_items, 'get_cart_total': cart_total}

    context = {'items': items, 'order': order}

    return render(request, 'store/checkout.html', context)


def update_cart(request, id):
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        quantity = int(quantity)
    else:
        quantity = 1

    if not request.user.is_authenticated:
        request.session.modified = True
        if not request.session.get('cart'):
            request.session['cart'] = {}

        if str(id) not in request.session.get('cart', {}):
            request.session['cart'][str(id)] = quantity
        else:
            request.session['cart'][str(id)] += quantity

        return redirect('store')

    customer = request.user.customer
    order = customer.order_set.first()
    product = Product.objects.get(pk=id)

    if product.orderitem_set.first() not in order.orderitem_set.all():
        item = OrderItem(order=order, quantity=quantity, product=product)
        item.save()
    else:
        item = OrderItem.objects.get(order=order, product=product)
        item.quantity += quantity
        item.save()

    return redirect('store')


def add_item(request, id):
    if not request.user.is_authenticated:
        request.session.modified = True

        if not request.session.get('cart'):
            request.session['cart'] = {}

        request.session['cart'][str(id)] += 1

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
        request.session.modified = True

        if not request.session.get('cart'):
            request.session['cart'] = {}

        request.session['cart'][str(id)] -= 1

        if request.session['cart'][str(id)] == 0:
            del request.session['cart'][str(id)]

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

def product_details(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {'product': product}

    return render(request, 'store/product_details.html', context)
