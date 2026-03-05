from django.db import models
from django.conf import settings


class Task(models.Model):

    STATUS_CHOICES = [
        ("todo", "To Do"),
        ("inprogress", "In Progress"),
        ("complete", "Complete"),
    ]

    list = models.ForeignKey('List.List',on_delete=models.CASCADE,related_name='tasks')

    title = models.CharField(max_length=255)

    creator = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,
             related_name='created_tasks'
    )

    assignee = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,
        related_name='assigned_tasks'
    )

    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='subtasks')


    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="todo"
    )

    view_count = models.IntegerField(default=0)

    due_date = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    # Due Day auto generate
    def due_day(self):
        if self.due_date:
            return self.due_date.strftime("%A")
        return None

    def __str__(self):
        return self.title