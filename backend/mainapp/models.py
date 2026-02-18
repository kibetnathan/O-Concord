from django.utils import timezone
from django.db import models
from django.conf import settings
from userapp.models import Profile
from cloudinary.models import CloudinaryField
# Models for the main app 
class LeadershipTeam(models.Model):
    # Leadership teams in practice shouldn't have leaders
    name = models.CharField(max_length=255)
    description = models.TextField()
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="leadership_teams"
    )

    def __str__(self):
        return self.name
    
class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    leader = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="serving_team_leader",
        on_delete=models.SET_NULL,
        null=True,
    )
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="serving_team",
        blank=True
    )

class Services(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="services"
    )
    # A department can be part of a service, but it's not required, and a department can be part of multiple services, so we use a many-to-many relationship
    crew = models.ManyToManyField(
        Department,
        related_name="services_crew",
        blank=True
    )
    # pastors are seperate from the age group members
    pastor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="services_pastor"
    )

    def __str__(self):
        return self.name

    @property
    def equipment(self):
        return getattr(self, "assigned_equipment", None)
    
class Equipment(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.PositiveIntegerField(default=1)
    # if the equipment is assigned to a service, it can't be assigned to another service,
    image = CloudinaryField('image', blank=True, null=True)
    # The equipment can either be assigned to a service or a department, but not both, so we use a one-to-one relationship for both, and allow nulls
    assigned_service = models.OneToOneField(
        Services,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_equipment"
    )
    assigned_department = models.OneToOneField(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_equipment"
    )
# Services
class FellowshipGroup(models.Model):
    # in dgs leaders are also members
    name = models.CharField(max_length=255)
    description = models.TextField()
    leader = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="discipleship_group_leader"
    )
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="discipleship_group",
        blank=True
    )
    # The leader is included in the members, so we override the save method to ensure that the leader is always a member of the group, even if they are not explicitly added as a member when creating or updating the group
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.leader not in self.members.all():
            self.members.add(self.leader)

    def __str__(self):
        return (f'{self.name} led by {self.leader}')
    
    def get_leader(self):
        return self.leader

class Course(models.Model):
    # This is a class for courses and classes that most churches usually have, see more in the docs folder
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField(default=timezone.now)
    # duration in weeks, we can calculate the end date based on the start date and the duration, but we store the duration in weeks because it's easier to understand and work with for most people, and we can always convert it to days if needed
    expected_duration= models.DurationField(help_text="Expected duration of the course in weeks")
    leader = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="ropes_class_leader",
        on_delete=models.SET_NULL,
        null=True,
    )
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="ropes_class",
        blank=True
    )


# Data collection models

# This model was initially meant to cath the rest of the data that didn't fit into other models, but at the moment has been commented
# out because a use case has not been found yet
# class MinistryData(models.Model):
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         related_name="ministry_data",
#         on_delete=models.CASCADE,
#     )
#     @property
#     def name(self):
#         return f"{self.user.first_name} {self.user.last_name}"
#     @property
#     def campus(self):
#         if hasattr(self.user, "profile") and self.user.profile:
#             return self.user.profile.campus
#         return None
#     dg = models.ForeignKey(
#         DiscipleshipGroup,
#         on_delete=models.SET_NULL,
#         null=True,
#         related_name="dg"
#     )
#     department = models.ManyToManyField(
#         ServingTeam,
#         blank=True,
#         related_name="department"
#     )