from django.shortcuts import render, get_object_or_404, redirect
from .models import UploadedFile, FileAccess
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User


# Create your views here.


@login_required(login_url='signin')

def file_list(request):
    user = request.user
    print(user)
      # Récupérer les fichiers auxquels l'utilisateur a accès
    accessible_files = UploadedFile.objects.filter(fileaccess__user=user, fileaccess__has_access=True)
    print(accessible_files)
    #files = UploadedFile.objects.all()
    role = request.user.userprofile.role 
    return render(request, 'cruds/file_list.html', {'files':accessible_files, 'user_role': role})
@login_required(login_url='signin')



@login_required(login_url='signin')
def upload_file(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        file = request.FILES.get('file')
        description = request.POST.get('description')
        created = datetime.now()

        if title and file:
            uploaded_file = UploadedFile.objects.create(title=title, file=file, description=description, cerated=created)



            # Obtenir la liste des ID des utilisateurs sélectionnés
            selected_user_ids = request.POST.getlist('users_with_access')
            # Convertir les ID en entiers
            selected_user_ids = [int(user_id) for user_id in selected_user_ids]
            
            # Obtenir les objets User correspondants aux ID sélectionnés
            users_with_access = User.objects.filter(id__in=selected_user_ids)
            
            # Enregistrer les droits d'accès dans la base de données
            for user in users_with_access:
                file_access = FileAccess.objects.create(user=user, file=uploaded_file)                
                file_access.has_access = True  
                file_access.save()

            return HttpResponseRedirect(reverse('file_list'))
        else:
            error_message = "Title and file are required."
            return render(request, 'cruds/upload_file.html', {'error_message': error_message})
        
    
    # Obtenir la liste des utilisateurs qui ont les droits nécessaires pour passer à la vue
    users_with_access = User.objects.all()  # Vous pouvez personnaliser cela en fonction de vos critères
    return render(request, 'cruds/upload_file.html', {'users_with_access': users_with_access})




def delete_file(request, pk):
    file = get_object_or_404(UploadedFile, pk=pk)
    file.delete()
    return redirect('file_list')
