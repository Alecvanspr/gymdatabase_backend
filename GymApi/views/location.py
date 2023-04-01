from rest_framework import viewsets
from ..models import Location
from ..serializers.Location import LocationSerializer
from django.contrib.auth.models import User

class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer

    def get_queryset(self):
        queryset = Location.objects.all()
        location = self.request.query_params.get('location', None)
        if location is not None:
            queryset = queryset.filter(name=location)
        return queryset
    
    def perform_create(self,serializer):
        user = User.objects.get(pk=self.request.data['created_by'])
        serializer.save(created_by=user)