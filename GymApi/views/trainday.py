from rest_framework import viewsets
from rest_framework.response import Response
from ..models import Trainday
from ..serializers.Trainday import TraindaySerializer
from django.contrib.auth.models import User

class TraindayViewSet(viewsets.ModelViewSet):
    serializer_class = TraindaySerializer

    def get_queryset(self):
        queryset = Trainday.objects.all()
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
            train_day = Trainday.objects.all()
            serializer = TraindaySerializer(train_day, many=True)
            return Response(serializer.data)
        else:
            train_day = Trainday.objects.get(id=id)
            serializer = TraindaySerializer(train_day)
            return Response(serializer.data)
