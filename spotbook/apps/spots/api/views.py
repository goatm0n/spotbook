from rest_framework.decorators import api_view
from rest_framework.response import Response
from spotbook.apps.spots.models import Spot
from .serializers import SpotSerializer

@api_view(['GET'])
def overview(request):
    api_urls = {
        'List': '/list/',
        'Detail View': '/detail/<str:pk>/',
        'Create': '/create/',
        'Update': '/update/<str:pk>/',
        'Delete': '/delete/<str:pk>/',
    }
    
    return Response(api_urls)

@api_view(['GET'])
def list(request):
    spotList = Spot.objects.all().order_by('-id')
    serializer = SpotSerializer(spotList, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def detail(request, pk):
    spot = Spot.objects.get(id=pk)
    serializer = SpotSerializer(spot, many=False)

    return Response(serializer.data)
