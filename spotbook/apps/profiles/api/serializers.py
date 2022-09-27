from rest_framework import serializers
from spotbook.apps.profiles.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'user',
            'full_name',
            #'profile_picture',
            'bio',
            'followers'
        ]
