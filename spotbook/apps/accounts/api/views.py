from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/account-list/',
        'Detail View': '/account-detail/<str:pk>/',
        'Create': '/account-create/',
        'Update': '/account-update/<str:pk>/',
        'Delete': '/account-delete/<str:pk>/',
    }
    return Response(api_urls)
