from django.shortcuts import render, get_object_or_404, redirect
from .models import UploadedFile
from .forms import UploadedFileForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.


# def list(request):
#     pdf_documents = PdfDocument.objects.all()  # Récupérez tous les documents PDF
#     return render(request, 'cruds/list.html', {'pdf_documents': pdf_documents})

@login_required(login_url='signin')
def file_list(request):
    files = UploadedFile.objects.all()
    return render(request, 'cruds/file_list.html', {'files':files})
@login_required(login_url='signin')


# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadedFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('file_list')
#     else:
#         form = UploadedFileForm()
#     return render(request, 'cruds/upload_file.html', {'form': form})


@login_required(login_url='signin')
def upload_file(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        file = request.FILES.get('file')
        description = request.POST.get('description')
        created = datetime.now()

        if title and file:
            UploadedFile.objects.create(title=title, file=file, description=description, cerated=created)  # Correction ici
            return HttpResponseRedirect(reverse('file_list'))
        else:
            error_message = "Title and file are required."
            return render(request, 'cruds/upload_file.html', {'error_message': error_message})
    
    return render(request, 'cruds/upload_file.html')

def delete_file(request, pk):
    file = get_object_or_404(UploadedFile, pk=pk)
    file.delete()
    return redirect('file_list')
