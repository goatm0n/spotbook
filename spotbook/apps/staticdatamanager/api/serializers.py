from rest_framework import serializers
from spotbook.apps.staticdatamanager.models import GlobalKeyValuePair

class GlobalKeyValuePairSerializer():
    class Meta:
        model = GlobalKeyValuePair
        fields = [
            'domain_id',
            'service',
            'created_datetime',
            'updated_datetime',
            'entity_type',
            'key',
            'value',
            'list_name',
            'user_id',
        ]