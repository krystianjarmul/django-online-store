from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'store/main.html', context)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def store(request):
    context = {}
    return render(request, 'store/store.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)