from django.urls import path
from . import views

urlpatterns = [
    path('<str:domain_id>/<str:service_name>/keyvalues', views.get_tenant_service_gkvp_list, name='Tenant Service Key Values List'),
]