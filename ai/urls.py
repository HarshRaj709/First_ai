from django.contrib import admin
from django.urls import path,include
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title = 'First AI',
        default_version='v1',
        contact = openapi.Contact(email="harshsahu709@gmail.com")
    ),
    public = True,
    permission_classes = [permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('gemni.urls')),
    path('api/plan/',include('gemni.api.urls')),
    path('api/auth/',include('auth.api.urls')),
    path('swagger/',schema_view.with_ui(cache_timeout=0),name='swagger')
]
