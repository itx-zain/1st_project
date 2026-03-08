from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    total_time = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = "__all__"

    def get_total_time(self, obj):
        if obj.start_time and obj.end_time:
            return obj.end_time - obj.start_time
        return None