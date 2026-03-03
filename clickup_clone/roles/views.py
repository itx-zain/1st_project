from django.shortcuts import render
from rest_framework import viewsets
from .models import Role,Permission
from .serializers import RoleSerializer,PermissionSerializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer