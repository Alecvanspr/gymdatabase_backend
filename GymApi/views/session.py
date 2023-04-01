from rest_framework import viewsets
from rest_framework.response import Response
from ..models import Session
from ..serializers.session import SessionSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class SessionViewSet(viewsets.ModelViewSet):
    serializer_class = SessionSerializer

    def get_queryset(self):
        user = get_object_or_404(User, id=self.request.user.id)
        
        queryset = Session.objects.filter(created_by=user)
        date = self.request.query_params.get('date', None)
        if date is not None:
            queryset = queryset.filter(date=date)
        return queryset.order_by("-date")
    
    def perform_create(self, serializer):
        user = User.objects.get(pk=self.request.data['created_by'])
        serializer.save(created_by=user)
    
    def perform_update(self, serializer):
        serializer.save()
    
    def perform_destroy(self, instance):
        instance.delete()   
    
    def get (self, request, id):
        session = Session.objects.get(pk=id)
        serializer = SessionSerializer(session)
        return Response(serializer.data)
    
    def get_list(self, request, user_id):
        user = User.objects.get(pk=user_id)
        session = Session.objects.filter(created_by=user).order_by("-date")
        serializer = SessionSerializer(session, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        return super().create(request)
    