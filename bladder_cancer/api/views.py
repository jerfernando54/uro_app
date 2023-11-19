from rest_framework.viewsets import ModelViewSet

from django_filters.rest_framework import DjangoFilterBackend 
from bladder_cancer.models import BladderCancer, History
from bladder_cancer.api.serializers import(
  BladderCancerSerializer, 
  HistorySerializer
)
from user.api.permissions import IsDoctorOrNurse
from bladder_cancer.api.permissions import IsDoctor, IsNotAuthorized

class BladderCancerModelViewSet(ModelViewSet):
  permission_classes = [IsDoctorOrNurse, IsDoctor]
  serializer_class = BladderCancerSerializer
  queryset = BladderCancer.objects.filter(is_active=True)
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['is_active', 'dni', 'edad']

class HistoryModelViewSet(ModelViewSet):
  permission_classes = [IsNotAuthorized]
  serializer_class = HistorySerializer
  queryset = History.objects.all()
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['hisID']