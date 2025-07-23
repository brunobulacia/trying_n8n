from rest_framework import serializers
from django.contrib.auth.models import User as Usuario



class UsuarioSerializer(serializers.ModelSerializer):
    is_staff = serializers.BooleanField(required=False)
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'password']
        # fields = '__all__'
        read_only_fields = ['id']
        
 