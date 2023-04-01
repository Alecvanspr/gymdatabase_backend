from rest_framework import viewsets
from ..models import Set,Exercise
from ..serializers.set import SetSerializer, ExerciseSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class SetViewSet(viewsets.ModelViewSet):
    serializer_class = SetSerializer

    def get_queryset(self):
        #user = get_object_or_404(User, id=self.request.user.id)
        queryset = Set.objects.all()
        date = self.request.query_params.get('date', None)

        if date is not None:
            queryset = queryset.filter(session__date=date)
        return queryset
    
    def perform_create(self,serializer):
        user = User.objects.get(pk=self.request.data['created_by'])
        serializer.save(created_by=user)
    
    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def get_list_per_user(self, request, user_id):
        user = User.objects.get(pk=user_id)
        set = Set.objects.filter(created_by=user)
        serializer = SetSerializer(set, many=True)
        return Response(serializer.data)
    
class SetPerSession(viewsets.ModelViewSet):
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        queryset = Exercise.objects.all()
        queryset = queryset.filter(sets__session__id=self.kwargs['id']).distinct()

        return queryset
