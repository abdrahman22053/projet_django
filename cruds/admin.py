from django.contrib import admin
from .models import  UploadedFile, FileAccess


admin.site.register(UploadedFile)
admin.site.register(FileAccess)


# Register your models here.

