from rest_framework import viewsets
from ..models import MuscleGroup
from ..serializers.muscleGroup import MuscleGroupSerializer
from django.contrib.auth.models import User

class MuscleGroupViewSet(viewsets.ModelViewSet):
    serializer_class = MuscleGroupSerializer

    def get_queryset(self):
        queryset = MuscleGroup.objects.all()
        muscle_group = self.request.query_params.get('muscle_group', None)
        if muscle_group is not None:
            queryset = queryset.filter(name=muscle_group)
        return queryset

    def perform_create(self,serializer):
        user = User.objects.get(pk=self.request.data['created_by'])
        serializer.save(created_by=user)