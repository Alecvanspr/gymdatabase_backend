from rest_framework import viewsets
from ..models import Exercise
from    ..serializers.exercise import ExerciseSerializer
from django.contrib.auth.models import User

class ExerciseViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        queryset = Exercise.objects.all()
        muscle_group = self.request.query_params.get('muscle_group', None)
        
        if muscle_group is not None:
            queryset = queryset.filter(muscle_group__name=muscle_group)
        return queryset

    def perform_create(self,serializer):
        user = User.objects.get(pk=self.request.data['created_by'])
        serializer.save(created_by=user)