from django import forms
from django.contrib.auth.forms import UserCreationForm
from onlineform.models import User

class UserForm(UserCreationForm):  # Inherit from UserCreationForm for password hashing
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'date_of_birth']
