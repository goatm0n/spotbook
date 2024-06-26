from django.db import models
from spotbook import settings

User = settings.AUTH_USER_MODEL

class GlobalKeyValuePair(models.Model):
    domain_id = models.IntegerField()
    service = models.CharField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    entity_type = models.CharField()
    key = models.CharField()
    value = models.CharField()
    list_name = models.CharField()
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)


