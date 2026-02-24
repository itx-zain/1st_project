from django.db import models
from django.conf import settings


class Workspace(models.Model):
    name = models.CharField(max_length=255)

    


class WorkspaceMember(models.Model):
    workspace = models.ForeignKey('workspace.Workspace', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.workspace}"


class Role(models.Model):
    workspace = models.ForeignKey('workspace.Workspace', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

   


class Permission(models.Model):
    role = models.ForeignKey('workspace.Role', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

