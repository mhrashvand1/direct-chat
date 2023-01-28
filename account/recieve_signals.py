from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from account.models import Profile, OnlineStatus

User = get_user_model()

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    created = kwargs.get("created")
    if created:
        Profile.objects.create(user=instance)
        OnlineStatus.objects.create(user=instance)