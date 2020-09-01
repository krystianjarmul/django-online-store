from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import RegistrationForm

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
            return redirect("home")
        else:
            messages.error(request, "Username or password is incorrect.")

    return render(request, 'accounts/login.html')


def logout_page(request):
    logout(request)
    return redirect('login')


def index(request):
    return render(request, 'index.html')


def profile_page(request, pk):
    user = User.objects.get(id=pk)
    context = {"user": user}

    return render(request, 'accounts/profile.html', context)
