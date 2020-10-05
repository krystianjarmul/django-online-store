from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('store/', views.store, name='store'),
    path('store/<int:id>', views.product_details, name='product_details'),
    path('update-cart/<int:id>', views.update_cart, name='update_cart'),
    path('add-item/<int:id>', views.add_item, name="add_item"),
    path('remove-item/<int:id>', views.remove_item, name="remove_item"),
]