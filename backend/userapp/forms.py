from django.contrib.auth.forms import AdminUserCreationForm, UserChangeForm
from django_registration.forms import RegistrationForm
from .models import CustomUser

class CustomUserCreationForm(AdminUserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")
        
class CustomUserRegistrationForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")