from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from user.api.permissions import IsDoctorOrNurse
from bladder_cancer.models import BladderCancer
from bladder_cancer.api.serializers import BladderCancerSerializer
from prediction.api.serializers import BladderCancerPredictedSerializer
from trainingModels.predictionmodels import trainPredictModelBladderCancer
from constants import constants

class PredictionApiView(generics.RetrieveAPIView):
  permission_classes = [IsDoctorOrNurse]
  queryset = BladderCancer.objects.all()
  serializer_class = BladderCancerPredictedSerializer

  def post(self, request, paramID):
    if paramID is not None:
      try: 
        res = trainPredictModelBladderCancer([], paramID, True)
        return Response(status=status.HTTP_200_OK, data=res)
      except ValueError:
        return Response(status=status.HTTP_400_BAD_REQUEST, data=res) 
    return Response(status=status.HTTP_400_BAD_REQUEST, data=res) 

  def retrieve(self, request, *args, **kwargs):
    paramID = kwargs.get('paramID')
    
    try:
     paramID = int(paramID)
     if paramID <= 0:
       return Response(status = status.HTTP_400_BAD_REQUEST, data = 'El parámetro debe ser un número entero mayor que cero') 
    except ValueError:
      return Response(status = status.HTTP_400_BAD_REQUEST, data = 'El parámetro debe ser un número entero válido') 

    patient = get_object_or_404(self.queryset, id=paramID) 
    serializer = self.get_serializer(patient)
    patient_to_predict = [serializer.data]
    prediction = trainPredictModelBladderCancer(patient_to_predict, 1, False)
    
    if isinstance(prediction, list):
      numbers = [int(number) for number in prediction]
      print(numbers)
      res = {
        **serializer.data,
        'progresiva': constants.PROGRESIVASTATE[numbers[0]],
        'recidiva':constants.RECIDIVASTATE[numbers[1]],
        'exitus':constants.EXITUSSTATE[numbers[2]],
        'nrecidivas':numbers[3],
        'evoldesfavorable':constants.EVOLDESFAVORABLESTATE[numbers[4]],
      }
      return Response(status=status.HTTP_200_OK, data = res)

    return Response(status=status.HTTP_400_BAD_REQUEST, data = prediction)
  


    