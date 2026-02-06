from django.urls import path, include
from . import views
from .views import LeadershipTeamViewSet, AgeGroupViewSet, DiscipleshipGroupViewSet, RopesClassViewSet, ServingTeamViewSet, MinistryDataViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"leadership-team", LeadershipTeamViewSet)
router.register(r"age-group", AgeGroupViewSet)
router.register(r"discipleship-group", DiscipleshipGroupViewSet)
router.register(r"ropes-class", RopesClassViewSet)
router.register(r"serving-team", ServingTeamViewSet)
router.register(r"ministry-data", MinistryDataViewSet)


urlpatterns= [
    path('', views.index, name='index'),
    path('pastor', views.pastors, name='pastors'),
    path('', include(router.urls))
    # path('leadership-teams', LeadershipTeamView.as_view()),
    # path('age-groups', AgeGroupView.as_view()),
    # path('discipleship-groups', DiscipleshipGroupView.as_view()),
    # path('ropes-classes', RopesClassView.as_view()),
    # path('ministry-data', MinistryDataView.as_view()),
    # path('serving-team', ServingTeamView.as_view()),
]