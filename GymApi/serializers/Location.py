from rest_framework import serializers
from ..models import Location

class LocationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='__str__')

    class Meta:
        model = Location
        fields = ('id', 'name', 'organisation', 'street', 'place', 'zipcode', 'country')