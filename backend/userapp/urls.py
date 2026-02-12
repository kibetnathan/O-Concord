from django.urls import path, include
from .views import login_view, ProfileView, ProfileViewSet
from rest_framework import routers
from .views import RegistrationAPIView

router = routers.DefaultRouter()
router.register(r"profile", ProfileViewSet)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('profiles', ProfileView.as_view()),
    path("api/register/", RegistrationAPIView.as_view(), name="api_register"),
    path('api/', include(router.urls)),
]