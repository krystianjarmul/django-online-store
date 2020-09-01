from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'store/main.html', context)