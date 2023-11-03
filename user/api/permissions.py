from rest_framework.permissions import BasePermission
from user.models import User

class IsDoctorOrReadOnly(BasePermission):
  def has_permission(self, request, view):
    if request.method in ('POST', 'PATCH'):
      user_id = request.user.id
      if user_id is not None:
        try:
          user_doctor = User.objects.get(id=user_id)
        except User.DoesNotExist:
          return False
        role = user_doctor.role
        if role == 'medico':
          return True
      return False
    return True
  
class IsDoctorOrNurse(BasePermission):
  def has_permission(self, request, view):
    user_id = request.user.id
    if user_id is not None:
      try:
        user_auth = User.objects.get(id=user_id)
      except User.DoesNotExist:
        return False
      role = user_auth.role
      if role in ('medico', 'enfermero'):
        return True
      return False
    return False