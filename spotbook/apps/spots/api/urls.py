from django.urls import path
from . import views

urlpatterns = [
        path('', views.overview, name='overview'),
        path('list/', views.list, name='list'),
        path('detail/<str:pk>/', views.detail, name='detail'),
        path('create/', views.create, name='create'),
        path('like-toggle/<str:pk>/', views.like_toggle, name='like_toggle'),
        ]
