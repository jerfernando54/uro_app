from prediction.models import BladderCancerPrediction
from bladder_cancer.models import BladderCancer
from rest_framework import serializers

class PredictionTrainModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = BladderCancerPrediction
    fields = [
      'edad', 
      'sexo',
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
      'rtu'
    ]

class BladderCancerPredictedSerializer(serializers.ModelSerializer):
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
    ]