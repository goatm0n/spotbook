from rest_framework_gis.serializers import GeoFeatureModelSerializer
from spotbook.apps.spots.models import Spot, SpotList, SpotListItem
from rest_framework import serializers

class SpotSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Spot
        geo_field = 'location'
        fields = (
            'user',
            'title',
            'location',
            'spotType',
            'description',
            'id',
            'likes',
            'timestamp',
            'followers',
        )

class SpotListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotList
        fields = [
            'user',
            'name',
            'timestamp',
            'id',
        ]

class SpotListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotListItem
        fields = [
            'user',
            'spot',
            'spotlist',
            'timestamp',
            'id',
        ]