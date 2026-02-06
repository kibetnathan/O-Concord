from django.urls import path, include
from .views import login_view, ProfileView, ProfileViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"profile", ProfileViewSet)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('profiles', ProfileView.as_view()),
    path('', include(router.urls)),
]