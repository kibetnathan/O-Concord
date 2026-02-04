from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from django.conf import settings
from .models import CustomUser, Profile

User = settings.AUTH_USER_MODEL

@receiver(post_save, sender=User)
def assign_member_group(sender, instance, created, **kwargs):
    if created:
        member_group, _ = Group.objects.get_or_create(name="Member")
        instance.groups.add(member_group)
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Create a Profile automatically whenever a new CustomUser is created.
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    """
    Save the Profile whenever the CustomUser is saved.
    Useful if you ever modify user fields and want to ensure Profile sync.
    """
    if hasattr(instance, 'profile'):
        instance.profile.save()
