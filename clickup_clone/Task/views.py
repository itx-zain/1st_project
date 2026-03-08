from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


    @action(detail=True, methods=['post'])
    def start_task(self, request, pk=None):
        task = self.get_object()
        task.status = "inprogress"
        task.save()
        return Response({
            "message": "Task started",
            "start_time": task.start_time
        })

    # Optional: complete task manually via API
    @action(detail=True, methods=['post'])
    def complete_task(self, request, pk=None):
        task = self.get_object()
        task.status = "complete"
        task.save()
        return Response({
            "message": "Task completed",
            "end_time": task.end_time
        })