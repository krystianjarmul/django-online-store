from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import RegistrationForm
from store.models import Order, OrderItem, Product


def register_page(request):
    form = RegistrationForm()

    if request.method == 'POST':

        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}")

            return redirect('login')

    context = {'form': form}

    return render(request, 'accounts/register.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            if not user.is_authenticated:
                return redirect("home")

            cart = request.session.get('cart', {})
            order, craeted = Order.objects.get_or_create(customer=user.customer, complete=False)

            for id, quantity in cart.items():
                product = Product.objects.get(pk=id)

                order_item = OrderItem(product=product,
                                       order=order,
                                       quantity=quantity)

                logged_products = [item.product for item in order.orderitem_set.all()]

                if product in logged_products:
                    order_item = OrderItem.objects.get(product=product)
                    order_item.quantity += 1

                order_item.save()



            return redirect("home")
        else:
            messages.error(request, "Username or password is incorrect.")

    return render(request, 'accounts/login.html')

@login_required()
def logout_page(request):
    logout(request)
    return redirect('login')

@login_required()
def profile_page(request, pk):
    user = User.objects.get(id=pk)
    context = {"user": user}

    return render(request, 'accounts/profile.html', context)
