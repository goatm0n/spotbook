from rest_framework import serializers
from spotbook.apps.accounts.models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'email',
            'username',
            'password',
            'date_joined',
            'last_login',
            'is_admin',
            'is_active',
            'is_staff',
            'is_superuser',
            'id',
        ]
