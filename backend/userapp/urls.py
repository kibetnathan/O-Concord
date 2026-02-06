from django.urls import path
from .views import login_view, ProfileView

urlpatterns = [
    path('login/', login_view, name='login'),
    path('profiles', ProfileView.as_view())
]