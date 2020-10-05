import uuid

from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,
                                blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True,
                                 blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.UUIDField(default=uuid.uuid4, editable=True)

    def __str__(self):
        return str(self.transaction_id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()

        return sum([item.get_total for item in orderitems])

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()

        return sum([item.quantity for item in orderitems])


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True,
                                blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True,
                              blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.order.transaction_id, self.product.name)

    @property
    def get_total(self):
        return self.product.price * int(self.quantity)


class ShippingAddress(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True,
                                blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True,
                              blank=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    zip_code = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
