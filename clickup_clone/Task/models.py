from django.db import models
from django.conf import settings


class Task(models.Model):
    list = models.ForeignKey('List.List',on_delete=models.CASCADE,related_name='tasks')

    title = models.CharField(max_length=255)

    creator = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,
        related_name='created_tasks'
    )

    assignee = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,
        related_name='assigned_tasks'
    )

    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,
        related_name='subtasks'
    )

    created_at = models.DateTimeField(auto_now_add=True)

   