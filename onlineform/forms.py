from django.forms import ModelForm 
from onlineform.models import User

class UserForm(ModelForm):
    class Meta:
        model: User
        fields = ['first_name','last_name','phone_number','email','password','date_of_birth']