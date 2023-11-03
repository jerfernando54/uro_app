from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  # pass
  email = models.EmailField(unique=True)
  role = models.CharField(max_length=20)
  dni = models.CharField(max_length=20, unique=True)
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['role']