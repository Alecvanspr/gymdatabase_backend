from rest_framework import serializers
from ..models import Training

class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = ('id', 'name','muscle_groups','exercises','created_by')