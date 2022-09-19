from django.urls import path, include

urlpatterns = [
        path('api/', include('spotbook.apps.accounts.api.urls')),
        ]
