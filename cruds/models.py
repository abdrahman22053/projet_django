from django.db import models
from datetime import datetime


class UploadedFile(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/')
    cerated = models.DateTimeField(default=datetime.now)
    description = models.TextField(null=True, blank=True, verbose_name='Description')

    def __str__(self):
        return self.title
