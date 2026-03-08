from rest_framework import serializers
from .models import Sprint
from django.utils import timezone

class SprintSerializer(serializers.ModelSerializer):
    start_date = serializers.DateField(default=timezone.now().date)
    end_date = serializers.DateField(required=False)

    class Meta:
        model = Sprint
        fields = "__all__"

    def create(self, validated_data):
        if 'end_date' not in validated_data or validated_data['end_date'] is None:
            validated_data['end_date'] = validated_data['start_date'] + timezone.timedelta(days=5)
        return super().create(validated_data)