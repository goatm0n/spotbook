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
        'Update': '/update/<str:pk>/',
        'Delete': '/delete/<str:pk>/',
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

