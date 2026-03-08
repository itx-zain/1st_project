from django.db import models
from django.conf import settings
from django.utils import timezone


class Task(models.Model):

    STATUS_CHOICES = [
        ("todo", "To Do"),
        ("inprogress", "In Progress"),
        ("complete", "Complete"),
    ]

    list = models.ForeignKey(
        'List.List',
        on_delete=models.CASCADE,
        related_name='tasks'
    )

    sprint = models.ForeignKey(
        'sprint.Sprint',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tasks'
    )

    title = models.CharField(max_length=255)

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_tasks'
    )

    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='assigned_tasks'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="todo"
    )

    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)

    view_count = models.IntegerField(default=0)

    due_date = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):

        # jab task start ho
        if self.status == "inprogress" and not self.start_time:
            self.start_time = timezone.now()

        # jab task complete ho
        if self.status == "complete" and not self.end_time:
            self.end_time = timezone.now()

        super().save(*args, **kwargs)