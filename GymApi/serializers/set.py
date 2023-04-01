from rest_framework import serializers
from ..models import Set, Exercise
from django.contrib.auth.models import User

# class SetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Set
#         fields = ('id', 'session', 'exercise', 'weight', 'reps',)

class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = ('id' ,'weight', 'reps','exercise', 'session','set_count','created_by','device')

    
class ExerciseSerializer(serializers.ModelSerializer):
    sets = SetSerializer(many=True)

    class Meta:
        model = Exercise
        fields = ['id', 'name','sets',]