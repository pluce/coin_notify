from django.urls import path
from .views import AlertView
from rest_framework.urlpatterns import format_suffix_patterns

Alert_list = AlertView.as_view({
    'get' : 'list',
    'post' : 'create'
})

Alert_detail = AlertView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([

    path('alert/', Alert_list, name='alert-list'),
    path('alert/<int:pk>/', Alert_detail, name='alert-detail'),
])

