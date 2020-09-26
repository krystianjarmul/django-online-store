from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile
from store.models import Customer


@receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
def save_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = Profile(user=user)
        profile.save()

@receiver(post_save, sender=User, dispatch_uid='save_new_customer')
def save_customer(sender, instance, created, **kwargs):
    user = instance
    if created:
        customer = Customer(user=user, name=user.username)
        customer.save()
