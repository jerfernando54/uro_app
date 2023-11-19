from rest_framework.routers import DefaultRouter
from django.urls import path
from bladder_cancer.api.views import BladderCancerModelViewSet, HistoryModelViewSet


router_bladdercancer = DefaultRouter()

router_bladdercancer.register(prefix='bladdercancer', basename='bladdercancer', viewset=BladderCancerModelViewSet)
router_bladdercancer.register(prefix='histories', basename='histories', viewset=HistoryModelViewSet)


