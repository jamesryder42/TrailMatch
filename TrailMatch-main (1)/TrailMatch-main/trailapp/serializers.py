from rest_framework_json_api import serializers
from trailapp.models import Trail

class TrailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trail
        fields = ('trail_name', 'difficulty', 'trail_length','maps_link')
