from django.urls import path
from django.conf.urls import url

from core.apps.services.views import *

from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Letsbecool Task API",
      default_version='v1',
      description="API for Todo App",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="osmanuribuker@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerify.as_view(), name='token_verify'),
    path('todo', TodoCreate.as_view(), name='create_todo'),
    path('todos', TodoList.as_view(), name='get_all_todos'),
    path('todo/<int:pk>', TodoDetail.as_view(), name='single_todo')
]