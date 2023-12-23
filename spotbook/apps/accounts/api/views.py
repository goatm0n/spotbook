from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AccountSerializer
from spotbook.apps.accounts.models import Account


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/list/',
        'Detail View': '/detail/<str:pk>/',
        'Create': '/create/',
    }
    return Response(api_urls)

@api_view(['GET'])
def accountList(request):
    accountList = Account.objects.all().order_by('-id')
    serializer = AccountSerializer(accountList, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def accountDetail(request, pk):
    account = Account.objects.get(id=pk)
    serializer = AccountSerializer(account, many=False)

    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        email = request.data['email']
        username = request.data['username']
        password = request.data['password']
        Account.objects.create_user(email, username, password)
        return Response(serializer.data, status=201)
    return Response({}, status=400)

@api_view(['GET'])
def username(request, pk):
    account = Account.objects.get(id=pk)
    return Response({account.username})

@api_view(['PUT'])
def update(request, pk):
    try:
        account = Account.objects.get(id=pk)
    except:
        return Response(status=404)
    serializer = AccountSerializer(account, request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=204)
    return Response(status=404)
    
    





        




