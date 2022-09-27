from django.urls import path
from . import views

urlpatterns = [
    path('', views.overview, name='overview'),
    path('list/', views.list, name='list'),
    path('list-user/<str:username>/', views.list_user, name='list-by-user'),
    path('list-spot/<str:pk>/', views.list_spot, name='list-by-spot'),
    path('detail/<str:pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('likes/<str:pk>/', views.likes, name='likes'),
    
]
