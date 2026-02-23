from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Folder
from .serializers import FolderSerializer


class FolderViewSet(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer