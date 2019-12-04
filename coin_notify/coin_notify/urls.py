from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from rest_framework.authentication import BasicAuthentication
from django.conf.urls.static import static
from coin_notify import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('openapi', get_schema_view(
        title="CoinNotify",
        description="cryptocurrency notification API",
        version="0.1.0",
        authentication_classes=[BasicAuthentication],
    ), name='openapi-schema'),

    path('api/doc/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
] + static(settings.STATIC_URL)
