from django.urls import path
from api import views
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework import routers
from django.urls import include

schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version='v1',
        description="API para realizar operações CRUD em um blog",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("lista/", views.PostView.as_view(), name='lista-posts'),
    path('umpost/', views.PostView.as_view(), name='um-post'),
    path('umpost/<id_arg>/', views.PostView.as_view(), name='consulta-carro'),
    path("swagger/", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("swagger(<format>\.json|\.yaml)", schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path("redoc/", schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("api/v1/", include(routers.DefaultRouter().urls)),
    path("openapi/", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("schema/", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]