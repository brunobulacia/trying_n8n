from rest_framework import serializers
from django.contrib.auth.models import User as Usuario



class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'password']
        read_only_fields = ['id']

 