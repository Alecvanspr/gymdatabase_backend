from rest_framework import viewsets
from ..models import Equipment
from ..serializers.equiment import EquipmentSerializer
from django.contrib.auth.models import User

class EquipmentViewSet(viewsets.ModelViewSet):
    serializer_class = EquipmentSerializer

    def get_queryset(self):
        queryset = Equipment.objects.all()
        equipment = self.request.query_params.get('equipment', None)
        if equipment is not None:
            queryset = queryset.filter(name=equipment)
        return queryset
    
    def perform_create(self,serializer):
        user = User.objects.get(pk=self.request.data['created_by'])
        serializer.save(created_by=user)