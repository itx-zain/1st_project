from django.db import models


class Folder(models.Model):
    space = models.ForeignKey('space.Space',on_delete=models.CASCADE,related_name='folders')
    name = models.CharField(max_length=255)

    