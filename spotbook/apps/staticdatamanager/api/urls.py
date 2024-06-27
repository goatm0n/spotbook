from django.urls import path
from . import views

urlpatterns = [
    path('keyvalues/<str:domain_id>/<str:service_name>/', views.get_tenant_service_gkvp_list, name='All Global Key Value Pairs for Tenant and Service'),
    path('keyvalues/create/', views.create_gkvp, name='Create Global Key Value Pair'),
]