from django.shortcuts import render
from rest_framework import viewsets
from .models import Tarea
from .serializers import TareaSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = TareaSerializer
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return Tarea.objects.all()
        return Tarea.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        print(self.request.user)
        print(serializer)
        serializer.save(user=self.request.user)