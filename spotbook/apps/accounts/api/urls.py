from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='overview'),
    path('list/', views.accountList, name='list'),
    path('detail/<str:pk>/', views.accountDetail, name='detail'),
    path('create/', views.create, name='create'),
]
