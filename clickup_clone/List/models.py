from django.db import models


class List(models.Model):
    folder = models.ForeignKey('Folder.Folder',on_delete=models.CASCADE,related_name='lists')
    name = models.CharField(max_length=255)

    