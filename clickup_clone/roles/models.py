from django.db import models
from django.contrib.auth.models import User



class Role(models.Model):
    workspace = models.ForeignKey('workspace.Workspace', on_delete=models.CASCADE, related_name="roles")
    name = models.CharField(max_length=100)



class Permission(models.Model):
    role = models.ForeignKey('roles.Role', on_delete=models.CASCADE, related_name="permissions")
    name = models.CharField(max_length=100)

