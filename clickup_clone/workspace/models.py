from django.db import models
from django.utils import timezone
from django.conf import settings


class WorkspaceManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class Workspace(models.Model):
    name = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    objects = WorkspaceManager()
    all_objects = models.Manager()

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()



class WorkspaceMember(models.Model):
    workspace = models.ForeignKey('workspace.Workspace',on_delete=models.CASCADE,related_name="members")
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.workspace}"