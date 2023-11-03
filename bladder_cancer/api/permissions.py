from rest_framework.permissions import BasePermission
from user.models import User

class IsDoctor(BasePermission):
  def has_permission(self, request, view):
    if request.method in ('DELETE', 'PATCH'):
      user_id_authententicated = request.user.id
      if user_id_authententicated is not None:
        try:
          user = User.objects.get(id = user_id_authententicated)
        except User.DoesNotExist:
          return False
        user_role = user.role
        if user_role == 'medico':
          return True
        return False
      return False
    return True  
