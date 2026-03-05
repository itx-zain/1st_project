from rest_framework import viewsets
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


    def retrieve(self, request, *args, **kwargs):
        """
        Jab task detail view ho, view_count automatically increase ho jaye
        """
        task = self.get_object()
        task.view_count += 1
        task.save()

        serializer = self.get_serializer(task)
        return Response(serializer.data)