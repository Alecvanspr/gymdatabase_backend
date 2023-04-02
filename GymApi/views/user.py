from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from ..models import PersonalInformation, Weight

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.pk, 'email': user.email})
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def logout(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = make_password(request.data.get('password'))
    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        user = User.objects.create(username=username, email=email, password=password)
        user.save()
        birthdate = request.data.get('birthDate')
        gender = request.data.get("gender")
        height = request.data.get('height')
        weight = request.data.get('weight')
        personalinformation = PersonalInformation.objects.create(user=user,birthdate=birthdate, gender=gender, height=height)
        personalinformation.save()
        weight = Weight.objects.create(user=user, weight=weight)
        weight.save()
        return Response({'success': 'User created successfully','userid':user.id}, status=status.HTTP_201_CREATED)
