from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = SpotSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response({}, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_toggle(request, pk):
    qs = Spot.objects.filter(id=pk)
    
    if not qs.exists():
        return Response({}, status=404)

    obj = qs.first()
    
    if request.user in obj.likes.all():
        obj.likes.remove(request.user)
    else:
        obj.likes.add(request.user)

    return Response({}, status=201)


