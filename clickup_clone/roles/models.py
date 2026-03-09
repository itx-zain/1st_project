from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    workspace = models.ForeignKey('workspace.Workspace', on_delete=models.CASCADE, related_name="roles")
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.workspace})"


class Permission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="permissions")
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.role.name}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="roles_userprofile")
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} ({self.role})"