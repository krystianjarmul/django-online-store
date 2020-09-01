from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=9, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(null=True, blank=True, default="default_picture.png")

