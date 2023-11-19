from django.urls import path
from user.api.views import (
  RegisterView, 
  UserView, 
  BajaUserView, 
  UserUpdatePasswordView, 
  UserDNIView,
  PatientDataView
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
  path('auth/user', UserView.as_view()),
  path('auth/user/<str:user_dni>', UserDNIView.as_view()),
  path('auth/register/', RegisterView.as_view()),
  path('auth/login', TokenObtainPairView.as_view()),
  path('auth/token/refesh', TokenRefreshView.as_view()),
  path('user/clinical_history/<str:user_dni>', PatientDataView.as_view()),
  path('auth/baja/<int:user_id>', BajaUserView.as_view()),
  path('auth/user/update_password', UserUpdatePasswordView.as_view()),
]