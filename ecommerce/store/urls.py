from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('store/', views.store, name='store'),
    path('update-cart/<int:id>', views.update_cart, name='update_cart'),
]