from django.urls import path
from prediction.api.views import PredictionApiView

urlpatterns = [
  path('prediction/trainmodel/<int:paramID>', PredictionApiView.as_view()),
]