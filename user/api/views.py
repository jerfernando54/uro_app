from user.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q

from user.api.serializer import (
  UserSerializer,
  UserBajaSerializer,
  UserUpdateSerializer,
  UserRegisterSerializer,
  UserUpdatePasswordSerializer
)

from bladder_cancer.models import BladderCancer
from bladder_cancer.api.serializers import BladderCancerBajaAltaSerializer, BladderCancerSerializer
from rest_framework.permissions import IsAuthenticated
from user.api.permissions import IsDoctorOrReadOnly, IsDoctorOrNurse
from constants import constants

class RegisterView(APIView):
  def post(self, request):
    patient_dni = request.data.get('dni')
    user_role = request.data.get('role')
    if user_role == 'paciente':
      bladder_cancer = BladderCancer.objects.filter(dni = patient_dni).first()
      if bladder_cancer is not None:
        serializer = UserRegisterSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
          serializer.save()
          return Response(status=status.HTTP_201_CREATED, data='El usuario ha sido registrado correctamente')
      return Response(status=status.HTTP_400_BAD_REQUEST, data=constants.DNI_NOT_FOUND)
    else:
      serializer = UserRegisterSerializer(data = request.data)
      if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data='El usuario ha sido registrado correctamente')
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class UserView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request):
    serializer = UserSerializer(request.user)
    return Response(status=status.HTTP_200_OK, data=serializer.data)
  
  def put(self, request):
    user = User.objects.get(id=request.user.id)
    serializer = UserUpdateSerializer(user, request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(status=status.HTTP_200_OK, data='user updated')
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserUpdatePasswordView(APIView):
  permission_classes = [IsAuthenticated]

  def put(self, request):
    user = User.objects.get(id=request.user.id)
    serializer = UserUpdatePasswordSerializer(user, request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(status=status.HTTP_200_OK, data='Password updated')
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDNIView(APIView):
  permission_classes = [IsDoctorOrNurse]
  def get(self, request, user_dni):
    user = User.objects.get(Q(dni=user_dni) | Q(id=user_dni))
    serializer = UserSerializer(user)
    return Response(status=status.HTTP_200_OK, data=serializer.data)
  
class PatientDataView(APIView):
  permission_classes = [IsAuthenticated]
  def get(self, request, user_dni): 
    patient = BladderCancer.objects.get(dni = user_dni)
    serializer = BladderCancerSerializer(patient)
    return Response(status=status.HTTP_200_OK, data=serializer.data)


class BajaUserView(APIView):
  permission_classes = [IsDoctorOrReadOnly]

  def patch(self, request, user_id): 
    user = User.objects.get(id = user_id)
    bladder_cancer =  BladderCancer.objects.filter(dni = user.dni).first()
    bladder_serializer = BladderCancerBajaAltaSerializer(bladder_cancer, request.data)
    serializer = UserBajaSerializer(user, request.data)

    if bladder_serializer.is_valid(raise_exception=True):
      bladder_serializer.save()    
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(status=status.HTTP_200_OK, data='User updated')
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)