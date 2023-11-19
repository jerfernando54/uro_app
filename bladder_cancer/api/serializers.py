from rest_framework import serializers
from bladder_cancer.models import BladderCancer, History

class BladderCancerSerializer(serializers.ModelSerializer):
  class Meta:
    model = BladderCancer
    fields = [
      'id',
      'dni',
      'nhis',
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

class HistorySerializer(serializers.ModelSerializer):
  class Meta:
    model = History
    fields = [
      'created_at',
      'id',
      'hisID',
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
    ]




