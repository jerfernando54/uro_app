from rest_framework.permissions import BasePermission
from user.models import User

class IsDoctor(BasePermission):
  def has_permission(self, request, view):
    if request.method in ('DELETE', 'PATCH', 'PUT'):
      user_id_authenticated = request.user.id
      if user_id_authenticated is not None:
        try:
          user = User.objects.get(id = user_id_authenticated)
        except User.DoesNotExist:
          return False
        user_role = user.role
        if user_role == 'Medico':
          return True
        return False
      return False
    return True  
  
class IsNotAuthorized(BasePermission):
  def has_permission(self, request, view):
    if request.method in ('DELETE', 'PATCH', 'PUT'):
      return False 
    else:
      user_id_authenticated = request.user.id   
      if user_id_authenticated is not None:
        try:
          user = User.objects.get(id = user_id_authenticated)
        except User.DoesNotExist:
          return False
        user_role = user.role
        if user_role == 'Medico' or user_role == 'Enfermero':
          return True
        return False
      return False
