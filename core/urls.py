from django.urls import path
from .views import site, api


app_name = 'core'

urlpatterns = [
    path('api/', api.CandiitateApiViewSet.as_view({
    'get': 'list',
    'post': 'create',
    }), name='api_list'),
    path('api/<int:pk>/', api.CandiitateApiViewSet.as_view(
    {
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy',
    }
    ), name='api_detail'),
    
]
