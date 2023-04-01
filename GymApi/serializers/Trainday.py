from rest_framework import serializers
from ..models import Trainday

class TraindaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainday
        fields = ('id', 'name','muscle_groups','Exercises','created_by')