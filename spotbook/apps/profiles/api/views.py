from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from spotbook.apps.profiles.models import Profile
from django.http.response import Http404
from django.contrib.auth import get_user_model
from spotbook.apps.accounts.api.serializers import AccountSerializer
from .serializers import ProfileSerializer
from django.conf import settings
from rest_framework import status

User = get_user_model()

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'list': '/list/',
        'detail': '/detail/<str:username>/',
        'detail by user_id': 'user-id-detail/<str:pk>/',
        'followers': '/followers/<str:pk>/',
        'follow-toggle': '/follow-toggle/<str:username>/',
        'update': 'update/<str:pk>/',
        'get user id from email' : 'get-user-id-from-email/<str:email>',
    }
    return Response(api_urls)

@api_view(['GET'])
def list(request):
    profileList = Profile.objects.all().order_by('-id')
    serializer = ProfileSerializer(profileList, many=True)
    return Response(serializer.data)


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
def userIdDetail(request, pk):
    # get profile for passed userId
    qs = Profile.objects.filter(user=pk)
    if not qs.exists():
        raise Http404
    profile_obj = qs.first()
    serializer = ProfileSerializer(profile_obj)

    return Response(serializer.data)


@api_view(['GET'])
def followers(request, pk):
    qs = User.objects.filter(id=pk)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    profile = obj.profile
    followers = profile.followers.all()
    serializer = AccountSerializer(followers, many=True) 
    return Response(serializer.data, status=200)

@api_view(['GET'])
def followerProfiles(request, pk):
    qs = Profile.objects.filter(user=pk)
    if not qs.exists():
        return Response({}, status=404)
    profile = qs.first()
    follower_accounts = profile.followers.all()
    follower_profiles = Profile.objects.filter(user__in=follower_accounts)
    serializer = ProfileSerializer(follower_profiles, many=True)
    return Response(serializer.data, status=200)


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
def follow_toggle(request, pk):
    qs = Profile.objects.filter(user=pk)
    
    if not qs.exists():
        return Response({}, status=404)

    obj = qs.first()
    
    if request.user in obj.followers.all():
        obj.followers.remove(request.user)
    else:
        obj.followers.add(request.user)

    return Response({}, status=201)

@api_view(['GET'])
def does_user_follow(request, pk):
    qs = Profile.objects.filter(user=pk)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    user = request.user
    if user in obj.followers.all():
        return Response({'data': True}, status=200)
    else:
        return Response({'data': False}, status=200)
    
@api_view(['GET'])
def profile_picture(request, pk):
    profile = Profile.objects.get(user=pk)
    profile_picture = profile.profile_picture
    print(profile_picture)
    if not profile_picture:
        return Response({"src": settings.DEFAULT_PROFILE_PICTURE})
    else:
        return Response({"src": f'{settings.MEDIA_URL}{profile_picture}'})
    
    
@api_view(['GET'])
def user_id(request):
    return Response({"user_id": request.user.id})

@api_view(['GET'])
def getUserIdFromEmail(request, email):
    profile = Profile.objects.get(user__email=email)
    userId = profile.user.id
    return Response({"userId": userId})


@api_view(['GET'])
def default_profile_picture(request):
    return Response({"src": settings.DEFAULT_PROFILE_PICTURE})

@api_view(['PUT'])
def update(request, pk):
    profile = Profile.objects.get(user=pk)
    data = ProfileSerializer(instance=profile, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data=data.errors)

