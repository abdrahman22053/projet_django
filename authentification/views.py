from django.shortcuts import render, get_object_or_404

# Create your views here.


from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile
# Create your views here.


def home(request, *args, **kwargs):
    return render(request, 'authentification/signin.html')



from django.contrib.auth import login




def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, "This user doesn't exist.")
            return redirect('signin')
        
        authenticated_user = authenticate(username=username, password=password)
        
        if authenticated_user is not None:
            
            login(request, authenticated_user)
            request.session['is_auth'] = True
            # request.session['user_role'] = authenticated_user.userprofile.role



            # Rediriger en fonction du rôle de l'utilisateur
            if user.userprofile.role == 'Directeur de l\'informatique':
                return redirect('user_list')
                # request.session['role'] = 'admin'

            elif user.userprofile.role == 'Chef réseau':
                return redirect('file_list')
            
            else :
                return redirect('file_list')

        else:
            messages.error(request, 'Bad authentication. Please check your username and password.')
            return redirect('signin')

    return render(request, 'authentification/signin.html')


def signout(request):
    logout(request)
    request.session.clear()
    messages.success(request, 'logout successfully!')
    return redirect('signin')    




# usercrud

# @login_required(login_url='signin')
# def user_list(request):
#     user_profile = request.user.userprofile

#     # Si l'utilisateur est un chef de service, récupérez les subordonnés
#     if user_profile.role == 'Chef de service':
#         subordinates = user_profile.subordinates.all()
#         users = User.objects.filter(userprofile__in=subordinates)
#     # Si l'utilisateur est un directeur de l'informatique, récupérez les utilisateurs sous sa responsabilité
#     elif user_profile.role == 'Directeur de l\'informatique':
#         subordinates = UserProfile.objects.filter(chef=user_profile)
#         users = User.objects.filter(userprofile__in=subordinates)
#     # Si l'utilisateur est un chef réseau, récupérez les utilisateurs sous sa responsabilité
#     elif user_profile.role == 'Chef réseau':
#         subordinates = UserProfile.objects.filter(chef=user_profile)
#         users = User.objects.filter(userprofile__in=subordinates)
#     # Pour les autres rôles, affichez tous les utilisateurs
#     else:
#         users = User.objects.all()

#     return render(request, 'users/user_list.html', {'users': users, 'user_role': user_profile.role})

@login_required(login_url='signin')
def user_list(request):
    user_profile = request.user.userprofile
    users = []

    # Si l'utilisateur est un chef de service, récupérez les subordonnés
    if user_profile.role == 'Chef de service':
        users = User.objects.filter(userprofile__chef=user_profile)

    # Si l'utilisateur est un directeur de l'informatique, récupérez les utilisateurs sous sa responsabilité
    elif user_profile.role == 'Directeur de l\'informatique':
        subordinates = UserProfile.objects.filter(chef=user_profile)
        users = User.objects.filter(userprofile__in=subordinates)

    # Si l'utilisateur est un chef réseau, récupérez les utilisateurs sous sa responsabilité
    elif user_profile.role == 'Chef réseau':
        subordinates = UserProfile.objects.filter(chef=user_profile)
        users = User.objects.filter(userprofile__in=subordinates)

    # Pour les autres rôles, affichez tous les utilisateurs
    else:
        users = User.objects.all()

    return render(request, 'users/user_list.html', {'users': users, 'user_role': user_profile.role})




@login_required(login_url='signin')

def user_create(request):
    user_profile = request.user.userprofile

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']  
        role = request.POST['role']
        chef_id = request.POST.get('chef')  # Récupérer l'ID du chef depuis le formulaire

        # Vérifier si l'utilisateur existe déjà
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Un utilisateur avec ce nom d\'utilisateur existe déjà.')
            return render(request, 'users/user_create.html', {'roles': UserProfile._meta.get_field('role').choices})

        user = User.objects.create_user(username=username, password=password, email=email)
        
        # Attribuer le chef en fonction du rôle
        if user_profile.role == 'Chef de service':
            chef = UserProfile.objects.get(user_id=chef_id)
            UserProfile.objects.create(user=user, role=role, chef=chef)
        elif user_profile.role == 'Directeur de l\'informatique':
            chef = UserProfile.objects.get(user_id=chef_id)
            UserProfile.objects.create(user=user, role=role, chef=chef)
        elif user_profile.role == 'Chef réseau':
            chef = UserProfile.objects.get(user_id=chef_id)
            UserProfile.objects.create(user=user, role=role, chef=chef)
        else:
            UserProfile.objects.create(user=user, role=role)
            
        return redirect('user_list')
    
    # Obtenez la liste des profils d'utilisateurs ayant le rôle de chef
    chef_profiles = UserProfile.objects.filter(role__icontains="Chef")
    
    return render(request, 'users/user_create.html', {'roles': UserProfile._meta.get_field('role').choices, 'chef_profiles': chef_profiles})



@login_required(login_url='signin')



@login_required(login_url='signin')
def user_update(request, user_id):
    user = User.objects.get(id=user_id)
    profile = UserProfile.objects.get(user=user)
    
    if request.method == 'POST':
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.save()
        
        # Mise à jour du rôle et du chef en fonction du rôle de l'utilisateur connecté
        user_role = request.user.userprofile.role
        if user_role in ['Chef de service', 'Directeur de l\'informatique', 'Chef réseau']:
            profile.role = request.POST['role']
            if user_role != 'Utilisateur standard':
                profile.chef = request.user.userprofile
            profile.save()
        
        return redirect('user_list')
    
    return render(request, 'users/user_update.html', {'user': user, 'profile': profile, 'roles': UserProfile._meta.get_field('role').choices})


@login_required(login_url='signin')
def user_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile =  get_object_or_404(UserProfile, user=user)
    user.delete()
    profile.delete()
    return redirect('user_list')



