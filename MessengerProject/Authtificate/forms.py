from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserModel

class CreatUserForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")
