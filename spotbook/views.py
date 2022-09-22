from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework import views
from rest_framework.response import Response
from . import serializers

def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})

def ping(request):
    return JsonResponse({'result': 'OK'})


class LoginView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = serializers.LoginSerializer(
                data = self.request.data,
                context = { 'request': self.request }
                )
        print(serializer)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=202)
