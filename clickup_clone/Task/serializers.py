from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):

    due_day = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = "__all__"

    def get_due_day(self, obj):
        if obj.due_date:
            return obj.due_date.strftime("%A")
        return None