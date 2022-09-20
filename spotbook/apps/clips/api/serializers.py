from rest_framework import serializers
from spotbook.apps.clips.models import Clip

class ClipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clip
        fields = [
            'user',
            'spot',
            'textContent',
            'id',
            'likes',
        ]
