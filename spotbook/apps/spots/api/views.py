from ast import Return
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from spotbook.apps.spots.models import Spot, SpotList
from spotbook.apps.profiles.models import Profile
from spotbook.apps.profiles.api.serializers import ProfileSerializer
from .serializers import SpotListSerializer, SpotSerializer
from spotbook.apps.accounts.models import Account
from spotbook.apps.accounts.api.serializers import AccountSerializer

@api_view(['GET'])
def overview(request):
    api_urls = {
        'List': '/list/',
        'Detail': '/detail/<str:pk>/',
        'Create': '/create/',
        'Like': '/like-toggle/<str:pk>/',
        'Follow': '/follow-toggle/<str:pk>/',
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

@api_view(['GET'])
def likes(request, pk):
    qs = Spot.objects.filter(id=pk)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    likes = obj.likes.all()
    serializer = AccountSerializer(likes, many=True)
    return Response(serializer.data, status=200)

@api_view(['GET'])
def does_user_like(request, pk):
    qs = Spot.objects.filter(id=pk)
    if not qs.exists():
        return Response({}, status=404)
    spot = qs.first()
    user = request.user
    if user in spot.likes.all():
        return Response({'data': True}, status=200)
    else: 
        return Response({'data': False}, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_toggle(request, pk):
    qs = Spot.objects.filter(id=pk)
    
    if not qs.exists():
        return Response({}, status=404)

    obj = qs.first()
    
    if request.user in obj.followers.all():
        obj.followers.remove(request.user)
    else:
        obj.followers.add(request.user)

    return Response({}, status=201)

@api_view(['GET'])
def followers(request, pk):
    qs = Spot.objects.filter(id=pk)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    users = obj.followers.all()
    profiles = []
    for user in users:
        profiles.append(Profile.objects.get(user=user.id))
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
def does_user_follow(request, pk):
    qs = Spot.objects.filter(id=pk)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    user = request.user
    if user in obj.followers.all():
        return Response({'data': True}, status=200)
    else:
        return Response({'data': False}, status=200)

@api_view(['GET'])
def following(request, userId):
    qs = Account.objects.filter(id=userId)
    if not qs.exists():
        return Response({}, status=404)
    user = qs.first()
    spots = user.following_spots.all()
    serializer = SpotSerializer(spots, many=True)
    return Response(serializer.data, status=200)

@api_view(['GET'])
def spots_user_likes(request, userId):
    qs = Account.objects.filter(id=userId)
    if not qs.exists():
        return Response({}, status=404)
    user = qs.first()
    spots = user.spot_user.all()
    serializer = SpotSerializer(spots, many=True)
    return Response(serializer.data, status=200)

@api_view(['GET'])
def spotlists(request, userId):
    user_qs = Account.objects.filter(id=userId)
    if not user_qs.exists():
        return Response({}, status=404)
    user = user_qs.first()
    spotlists_qs = user.spotlist_set.all()
    serializer = SpotListSerializer(spotlists_qs, many=True)
    return Response(serializer.data, status=200)

@api_view(['GET'])
def spotlist(request, pk):
    qs = SpotList.objects.filter(id=pk)
    if not qs.exists():
        return Response({}, status=404)
    spotlist = qs.first()
    spotlistserializer = SpotListSerializer(spotlist, many=False)
    spotlistdata = spotlistserializer.data
    spotlistitem_qs = spotlist.spotlistitem_set.all()
    spots = [item.spot for item in spotlistitem_qs.all()]
    spotsserializer = SpotSerializer(spots, many=True)
    spotsdata = spotsserializer.data
    spotlistdata['spots'] = spotsdata

    return Response(spotlistdata, status=200)