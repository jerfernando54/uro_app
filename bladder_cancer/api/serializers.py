from rest_framework import serializers
from bladder_cancer.models import BladderCancer

class BladderCancerSerializer(serializers.ModelSerializer):
  class Meta:
    model = BladderCancer
    fields = [
      'id',
      'dni',
      'edad', 
      'sexo', 
      'fechacir',
      'obesidad',
      'hta',
      'dm',
      'tabaco',
      'hereda',
      'expoprofesional',
      'clinica',
      'citologias',
      'numtumores' ,
      'tamtumoral',
      'aspectotumoral',
      'estadotumoralclinico',
      'acarsinoinsitu',
      'gradotumoral',
      'permiacionvascular',
      'carcinomaUrotelial',
      'fhistoatipicas',
      'primario',
      'recidivante',
      'instalacionprevia',
      'tac',
      'rtu',
      'progresiva',
      'recidiva',
      'exitus',
      'nrecidivas',
      'evoldesfavorable',
      'is_active'
    ]
class BladderCancerBajaAltaSerializer(serializers.ModelSerializer):
  class Meta:
    model = BladderCancer
    fields = ['is_active']

