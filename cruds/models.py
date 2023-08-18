from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class UploadedFile(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/')
    cerated = models.DateTimeField(default=datetime.now)
    description = models.TextField(null=True, blank=True, verbose_name='Description')
    users_with_access = models.ManyToManyField(User, through='FileAccess')




    def __str__(self):
        return self.title


class FileAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.ForeignKey(UploadedFile, on_delete=models.CASCADE)
    has_access = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.user} - {self.file}"