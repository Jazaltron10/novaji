from django.db import models
# from django.contrib.auth.models import AbstractUser

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.PositiveIntegerField()
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=16)
    date_of_birth = models.DateField()
    
    # USERNAME_FIELD = ['email']
    # REQUIRED_FIELDS = ['email','password']
    
    


