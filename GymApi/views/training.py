from rest_framework import viewsets
from rest_framework.response import Response
from ..models import Training
from ..serializers.training import TrainingSerializer
from django.contrib.auth.models import User

class TraindayViewSet(viewsets.ModelViewSet):
    serializer_class = TrainingSerializer

    def get_queryset(self):
        queryset = Training.objects.all()
        train_day = self.request.query_params.get('train_day', None)
        if train_day is not None:
            queryset = queryset.filter(name=train_day)
        return queryset
    
    def perform_create(self,serializer):
        user = User.objects.get(pk=self.request.data['created_by'])
        serializer.save(created_by=user)
        
    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def get(self, request, id=None):
        if id is None:
            train_day = Training.objects.all()
            serializer = TrainingSerializer(train_day, many=True)
            return Response(serializer.data)
        else:
            train_day = Training.objects.get(id=id)
            serializer = TrainingSerializer(train_day)
            return Response(serializer.data)
