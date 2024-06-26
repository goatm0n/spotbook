from django.urls import path
from . import views

urlpatterns = [
    path('', views.overview, name='overview'),
    path('list/', views.list, name='list'),
    path('detail/<str:pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('like-toggle/<str:pk>/', views.like_toggle, name='like-toggle'),
    path('likes/<str:pk>/', views.likes, name='likes'),
    path('does-user-like/<str:pk>/', views.does_user_like, name='does user like spot'),
    path('follow-toggle/<str:pk>/', views.follow_toggle, name='follow-toggle'),
    path('followers/<str:pk>/', views.followers, name='followers'),
    path('does-user-follow/<str:pk>/', views.does_user_follow, name='does-user-follow-spot'),
    path('following/<str:userId>/', views.following, name="followed by user"),
    path('spots-user-likes/<str:userId>/', views.spots_user_likes, name="Spots User Likes"),
    path('spotlists/<str:userId>/', views.spotlists, name='spotslists'),
    path('spotlist/<str:pk>/', views.spotlist, name='spotlist'),
    path('create-spotlistitem/', views.createSpotListitem, name='create SpotListItem'),
    path('spotlistitems/<str:userId>/<str:spotId>/', views.spotlistItems, name='spot list items'),
    path('deletespotlistitem/<str:pk>/', views.deleteSpotListItem, name='delete spotlistitem'),
    path('createspotlist/', views.createSpotList, name='create spotlist'),
    path('deletespotlist/<str:pk>/', views.deleteSpotList, name='delete spotlist'),
    path('createspotlistuser/', views.createSpotListUser, name='create spotListUser'),
    path('deletespotlistuser/<str:userId>/', views.deleteSpotListUser, name='delete spotlistuser'),
    path('spotlistusers/<str:spotlistId>/', views.spotlistusers, name='list spotlistusers'),
    path('spotmapicon/<str:name>/', views.spotmapicon, name='spotmapicon'),
    path('spotmapiconlist/', views.spotmapiconlist, name='list spotmapicons'),
]
