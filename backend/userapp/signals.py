from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from django.conf import settings

User = settings.AUTH_USER_MODEL

@receiver(post_save, sender=User)
def assign_member_group(sender, instance, created, **kwargs):
    if created:
        member_group, _ = Group.objects.get_or_create(name="Member")
        instance.groups.add(member_group)
