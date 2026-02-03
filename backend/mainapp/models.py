from django.db import models
from django.conf import settings

# Create your models here.
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
    
class AgeGroup(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="age_group"
    )
    # pastors are seperate from the age group members
    pastor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="age_group_pastor"
    )

    def __str__(self):
        return self.name

class DiscipleshipGroup(models.Model):
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
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.leader not in self.members.all():
            self.members.add(self.leader)

    def __str__(self):
        return (f'{self.name} led by {self.leader}')
    
    def get_leader(self):
        return self.leader

class RopesClass(models.Model):
    # Ropes classes don't need a name or description, a leader and id are enough identification
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

class ServingTeam(models.Model):
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

# No campus trend model yet as the group structure is unknown