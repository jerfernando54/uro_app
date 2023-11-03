from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from bladder_cancer.api.router import router_bladdercancer
# from prediction.api.router import router_prediction

schema_view = get_schema_view(
   openapi.Info(
      title="Uro APP",
      default_version='v1',
      description="Entorno de testes",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="MIT"),
   ),
   public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('user.api.router')),
    path('api/', include(router_bladdercancer.urls)),
    path('api/', include('prediction.api.router')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
