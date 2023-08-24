from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='overview'),
    path('list/', views.list, name='list'),
    path('detail/<str:username>/', views.detail, name='detail'),
    #path('<str:username>/follow', views.user_follow_view, name='api-profile-follow'), 
    path('followers/<str:pk>/', views.followers, name='followers'),
    path('does-user-follow/<str:pk>/', views.does_user_follow, name='does-user-follow-profile'),
    path('following/<str:username>/', views.following, name='api-following-profiles-list'),
    #path('user-following-spots/<str:username>/', views.user_following_spots_list, name='api-user-following-spots-list'),
    path('follow-toggle/<str:pk>/', views.follow_toggle, name='follow-toggle'),
    path('user-id-detail/<str:pk>/', views.userIdDetail, name='userId detail'),
]
