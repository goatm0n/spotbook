from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from spotbook.apps.staticdatamanager.models import GlobalKeyValuePair
from spotbook.apps.staticdatamanager.api.serializers import GlobalKeyValuePairSerializer


@api_view(['GET'])
def get_tenant_service_gkvp_list(domain_id:int, service_name:str):
    qs = GlobalKeyValuePair.objects.filter(domain_id=domain_id, service_name=service_name)
    if not qs.exists():
        return Response({}, status=404)
    serializer = GlobalKeyValuePairSerializer(qs, many=True)
    return Response(serializer.data, status=200)

@api_view(['POST'])
@permission_classes([IsAdminUser]) # is_staff
def create_gkvp(request):
    serializer = GlobalKeyValuePairSerializer(request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response({}, status=400)