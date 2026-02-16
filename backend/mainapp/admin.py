from django.contrib import admin
from .models import LeadershipTeam, AgeGroup, DiscipleshipGroup, RopesClass, ServingTeam, MinistryData
# Register your models here.
@admin.register(AgeGroup)
class AgeGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'pastor')
    filter_horizontal = ('members',)  # nice multi-select for members

@admin.register(DiscipleshipGroup)
class DiscipleshipGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'leader')
    filter_horizontal = ('members',)

@admin.register(LeadershipTeam)
class LeadershipTeamAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('members',)

@admin.register(RopesClass)
class RopesClassAdmin(admin.ModelAdmin):
    filter_horizontal = ('members',)

@admin.register(ServingTeam)
class ServingTeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'leader')
    filter_horizontal = ('members',)

@admin.register(MinistryData)
class MinistryDataAdmin(admin.ModelAdmin):
    list_display = ('user', 'dg')
    filter_horizontal = ('department',)