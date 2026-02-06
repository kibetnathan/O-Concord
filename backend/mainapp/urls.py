from django.urls import path
from . import views
from .views import LeadershipTeamView, AgeGroupView, DiscipleshipGroupView, RopesClassView, ServingTeamView, MinistryDataView

urlpatterns= [
    path('', views.index, name='index'),
    path('leadership-teams', LeadershipTeamView.as_view()),
    path('age-groups', AgeGroupView.as_view()),
    path('discipleship-groups', DiscipleshipGroupView.as_view()),
    path('ropes-classes', RopesClassView.as_view()),
    path('ministry-data', MinistryDataView.as_view()),
    path('serving-team', ServingTeamView.as_view()),
]