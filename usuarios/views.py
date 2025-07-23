from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from rest_framework import viewsets
from django.contrib.auth.models import User as Usuario
from .serializers import UsuarioSerializer



@api_view(['POST'])
def register(request):
    serializer = UsuarioSerializer(data=request.data)
    if serializer.is_valid():
        password = serializer.validated_data['password']
        user = serializer.save()
        user.set_password(password)
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token' : token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    try:
        user = Usuario.objects.get(username=username)
        if user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)
            serializer = UsuarioSerializer(instance=user)
            return Response({'token': token.key, 'usuario' : serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    except Usuario.DoesNotExist:
        return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user = request.user
    serializer = UsuarioSerializer(instance=user)
    return Response(serializer.data, status=status.HTTP_200_OK)



class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

