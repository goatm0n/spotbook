from django.urls import path, include

urlpatterns = [
    path('api/', include('spotbook.apps.clips.api.urls')),
]
