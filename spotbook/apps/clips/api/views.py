from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from spotbook.apps.clips.models import Clip
from spotbook.apps.profiles.api.serializers import ProfileSerializer
from spotbook.apps.profiles.models import Profile
from .serializers import ClipSerializer
from spotbook.apps.accounts.api.serializers import AccountSerializer
from django.conf import settings

@api_view(['GET'])
def overview(request):
    api_urls = {
        'List': '/list/',
        'List by spot': '/list-spot/<str:pk>/',
        'List by user': '/list-user/<str:username>/',
        'Detail View': '/detail/<str:pk>/',
        'Create': '/create/',
        'Profile ClipFeed': '/profile-clipfeed/<str:pk>/',
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
def list_user_id(request, pk):
    clip_qs = Clip.objects.filter(user=pk)
    clip_id_list = []
    for obj in clip_qs:
        clip_id_list.insert(0, obj.id)
    
    return Response({"clip_id_list": clip_id_list})

@api_view(['GET'])
def list_spot(request, pk):
    clip_qs = Clip.objects.filter(spot__id=pk)
    clip_id_list = []
    for obj in clip_qs:
        clip_id_list.insert(0, obj.id)
    
    return Response({"clip_id_list": clip_id_list})


def get_detail(pk):
    clip = Clip.objects.get(id=pk)
    serializer = ClipSerializer(clip)
    data = serializer.data
    data['username'] = clip.user.username
    data['likesCount'] = clip.likes.all().count()
    profile = Profile.objects.get(user__username=data['username'])
    profile_serializer = ProfileSerializer(profile)
    profile_data = profile_serializer.data
    profile_picture = profile_data['profile_picture']
    data['profile_picture'] = profile_picture
    return data

@api_view(['GET'])
def detail(request, pk):
    return Response(get_detail(pk))

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = ClipSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response({}, status=400)

@api_view(['GET'])
def likes(request, pk):
    qs = Clip.objects.filter(id=pk)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    likes = obj.likes.all()
    serializer = AccountSerializer(likes, many=True)
    return Response(serializer.data, status=200)

@api_view(['GET'])
def doesUserLike(request, pk):
    qs = Clip.objects.filter(id=pk)
    if not qs.exists():
        return Response({}, status=404)
    clip = qs.first()
    user = request.user
    if user in clip.likes.all():
        return Response({'data': True}, status=200)
    else: 
        return Response({'data': False}, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_toggle(request, pk):
    qs = Clip.objects.filter(id=pk)
    
    if not qs.exists():
        return Response({}, status=404)

    obj = qs.first()
    
    if request.user in obj.likes.all():
        obj.likes.remove(request.user)
    else:
        obj.likes.add(request.user)

    return Response({}, status=201)


@api_view(['GET'])
def profile_clipfeed(request, userId):
    qs = Clip.objects.filter(user=userId)
    if not qs.exists():
        return Response({}, status=404)
    data = []
    for clip in qs:
        detail = get_detail(clip.id)
        data.append(detail)

    return Response(data)