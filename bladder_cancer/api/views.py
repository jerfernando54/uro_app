from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend 
from bladder_cancer.models import BladderCancer
from bladder_cancer.api.serializers import BladderCancerSerializer
from user.api.permissions import IsDoctorOrNurse
from bladder_cancer.api.permissions import IsDoctor

class BladderCancerModelViewSet(ModelViewSet):
  permission_classes = [IsDoctorOrNurse, IsDoctor]
  serializer_class = BladderCancerSerializer
  queryset = BladderCancer.objects.all()
  # queryset = BladderCancer.objects.filter(is_active=True)
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['is_active', 'dni', 'edad']