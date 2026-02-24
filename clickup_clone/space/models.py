from django.db import models


class Space(models.Model):
    workspace = models.ForeignKey('workspace.Workspace',on_delete=models.CASCADE,related_name='spaces')
    name = models.CharField(max_length=255)

  