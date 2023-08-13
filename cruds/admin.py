from django.contrib import admin
from .models import PdfDocument, UploadedFile


admin.site.register(PdfDocument)
admin.site.register(UploadedFile)

# Register your models here.
