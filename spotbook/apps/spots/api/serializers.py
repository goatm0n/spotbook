from rest_framework_gis.serializers import GeoFeatureModelSerializer
from spotbook.apps.spots.models import Spot

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