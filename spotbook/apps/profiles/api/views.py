from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from spotbook.apps.profiles.models import Profile
from django.http.response import Http404
from django.contrib.auth import get_user_model
from .serializers import ProfileSerializer

User = get_user_model()

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'detail': '/detail/<str:username>/',
        'followers': '/followers/<str:username>/',
        'follow-toggle': '/follow-toggle/<str:username>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def detail(request, username):
    # get profile for passed username
    qs = Profile.objects.filter(user__username=username)
    if not qs.exists():
        raise Http404
    profile_obj = qs.first()
    serializer = ProfileSerializer(profile_obj)

    return Response(serializer.data)

@api_view(['GET'])
def followers(request, username):
    user_qs = User.objects.filter(username=username)
    if not user_qs.exists():
        return Response({}, status=404)

    user_ = user_qs.first()
    profile_ = user_.profile
    
    followers_qs = profile_.followers.all()
    followers = []
    for profile in followers_qs:
        username_ = profile.username
        followers.append(username_)

    return Response({'followers': followers})

@api_view(['GET'])
def following(request, username):
    user_profile_qs = Profile.objects.filter(user__username=username)
    user_profile = user_profile_qs.first()
    user_following_users_qs = user_profile.user.following.all()

    profile_list = []

    for profile in user_following_users_qs:
        profile_list.append(profile.user.username)

    return Response({'following': profile_list})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_toggle(request, username):
    qs = Profile.objects.filter(user__username=username)
    
    if not qs.exists():
        return Response({}, status=404)

    obj = qs.first()
    
    if request.user in obj.followers.all():
        obj.followers.remove(request.user)
    else:
        obj.followers.add(request.user)

    return Response({}, status=201)




