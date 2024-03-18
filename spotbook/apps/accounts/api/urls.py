from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='overview'),
    path('list/', views.accountList, name='list'),
    path('detail/<str:pk>/', views.accountDetail, name='detail'),
    path('create/', views.create, name='create'),
    path('username/<str:pk>/', views.username, name="username"),
    path('update/<str:pk>/', views.update, name="update"),
    path('userslike/<str:username>/', views.usersLike, name='users like username'),
]
