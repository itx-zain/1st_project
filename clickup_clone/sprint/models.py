from django.db import models


class Sprint(models.Model):

    list = models.ForeignKey(
        'List.List',
        on_delete=models.CASCADE,
        related_name='sprints'
    )

    name = models.CharField(max_length=255)

    start_date = models.DateField()
    end_date = models.DateField()

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

