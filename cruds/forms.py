from django import forms
from .models import UploadedFile

class UploadedFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ('title', 'file', 'description')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre'}),
            'file': forms.FileInput(attrs={'class': 'form-control-file form-control-lg'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description...', 'style': 'resize: vertical; max-height: 150px; font-size: 14px;'})
        }

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name in self.fields:
                self.fields[field_name].label = False