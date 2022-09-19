from django.urls import path, include

urlpatterns = [
        path('api/', include('spotbook.apps.profiles.api.urls')),
        ]
