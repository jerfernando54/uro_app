from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

class User(AbstractUser):
  # pass
  email = models.EmailField(unique=True)
  role = models.CharField(max_length=20)
  dni = models.CharField(max_length=20, unique=True)
  # patientID = models.IntegerField()
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['role']

  def full_clean(self, *args, **kwargs):
    super().full_clean(self, *args, **kwargs)
    if not self.role:
      return ValidationError({'Rol': ['El campo "role" no puede estar vacío.']})