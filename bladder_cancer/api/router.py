from rest_framework.routers import DefaultRouter
from bladder_cancer.api.views import BladderCancerModelViewSet


router_bladdercancer = DefaultRouter()

router_bladdercancer.register(prefix='bladdercancer', basename='bladdercancer', viewset=BladderCancerModelViewSet)