from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Sprint
from .serializers import SprintSerializer


class SprintViewSet(viewsets.ModelViewSet):

    queryset = Sprint.objects.all()
    serializer_class = SprintSerializer


    @action(detail=True, methods=['get'])
    def progress(self, request, pk=None):

        sprint = self.get_object()

        total_tasks = sprint.tasks.count()
        completed_tasks = sprint.tasks.filter(status="complete").count()

        progress = 0

        if total_tasks > 0:
            progress = (completed_tasks / total_tasks) * 100

        data = {
            "sprint": sprint.name,
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "progress_percentage": progress
        }

        return Response(data)