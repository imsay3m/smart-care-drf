from django.shortcuts import render
from rest_framework import viewsets
from .models import Service
from .serializers import ServiceSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.

class ServiceViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset=Service.objects.all()
    serializer_class=ServiceSerializer