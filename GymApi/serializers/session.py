from rest_framework import serializers
from ..models import Session

class SessionSerializer(serializers.ModelSerializer):
    #location = serializers.SerializerMethodField()
    trainday_name = serializers.SerializerMethodField()
    muscle_groups = serializers.SerializerMethodField()
    location_name = serializers.SerializerMethodField()

    class Meta:
        model = Session
        fields = ('id', 'date', 'start_time','end_time','location','trainday','trainday_name','muscle_groups','location_name')
    
    def get_location_name(self,obj):
        if(obj.location == None):
            return "No location"
        return obj.location.street + " - " + obj.location.organisation
    
    def get_trainday_name(self,obj):
        return obj.trainday.name + " day"
    
    def get_muscle_groups(self,obj):
        return obj.trainday.muscle_groups.all().values_list('id', flat=True)