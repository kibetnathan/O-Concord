from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    class Roles(models.TextChoices):
        PASTOR = "PASTOR", "Pastor"
        LEADER = "LEADER", "Leader"
        DG_LEADER = "DG_LEADER", "DG_Leader"
        MEMBER = "MEMBER", "Member"

    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.MEMBER
    )

    def __str__(self):
        return self.username