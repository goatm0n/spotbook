from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from spotbook.apps.clips.models import Clip
from spotbook.apps.profiles.models import Profile
from .serializers import ClipSerializer

@api_view(['GET'])
def overview(request):
    api_urls = {
        'List': '/list/',
        'List by spot': '/list-spot/<str:pk>/',
        'List by user': '/list-user/<str:username>/',
        'Detail View': '/detail/<str:pk>/',
        'Create': '/create/',
    }
    return Response(api_urls)

@api_view(['GET'])
def list(request):
    clipList = Clip.objects.all().order_by('-id')
    serializer = ClipSerializer(clipList, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def list_user(request, username):
    clip_qs = Clip.objects.filter(user__username=username)
    clip_id_list = []
    for obj in clip_qs:
        clip_id_list.append(obj.id)
    
    return Response({"clip_id_list": clip_id_list})

@api_view(['GET'])
def list_spot(request, spot_id):
    clip_qs = Clip.objects.filter(spot__id=spot_id)
    clip_id_list = []
    for obj in clip_qs:
        clip_id_list.append(obj.id)
    
    return Response({"clip_id_list": clip_id_list})

@api_view(['GET'])
def detail(request, pk):
    clip = Clip.objects.get(id=pk)
    serializer = ClipSerializer(clip)
    data = serializer.data
    data['username'] = clip.user.username
    data['likesCount'] = clip.likes.all().count()
    return Response(data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = ClipSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response({}, status=400)


