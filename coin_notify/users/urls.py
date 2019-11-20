from django.urls import include, path
from .views import UsersView, TestAuthView
from rest_framework.urlpatterns import format_suffix_patterns

users_list = UsersView.as_view({
    'get' : 'list',
    'post' : 'create'
})

users_detail = UsersView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([

    path('users/', users_list, name='user-list'),
    path('users/<int:pk>/', users_detail, name='user-detail'),
    path('test_auth/', TestAuthView.as_view(), name='test_auth'),
])
