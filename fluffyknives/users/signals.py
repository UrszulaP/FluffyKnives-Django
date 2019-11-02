# need to import signals in ready function in UsersConfig class in apps.py

from django.db.models.signals import post_save # makes signal when the object is saved
from django.contrib.auth.models import User # built in User model
from django.dispatch import receiver # receiver - gets signal and performs some tasks
from .models import Profile

# creates a Profile when User object is created
@receiver(post_save, sender=User) # when a User is saved, send a signal 'post_save', which is recived by receiver - create_profile function
def create_profile(sender, instance, created, **kwargs): # receiver, takes arguments that post_save signal passes (instance of User)
    if created:
        Profile.objects.create(user=instance)

# saves the Profile when User object is saved
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()