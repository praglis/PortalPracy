from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# when a user is created send post_save signal, create_profile function is a receiver
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created: # if a user is created, create a profile for him/her
        Profile.objects.create(user=instance)

#save created profile in database
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
        instance.profile.save()
