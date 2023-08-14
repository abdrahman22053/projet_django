from django.shortcuts import render, get_object_or_404

# Create your views here.


from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.decorators import login_required
#from django.utils.encoding import force_bytes, force_text
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . tokens import generateToken
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


            # Rediriger en fonction du rôle de l'utilisateur
            if user.userprofile.role == 'Directeur de l\'informatique':
                return redirect('user_list')
                # request.session['role'] = 'admin'
            else:
                return redirect('file_list')

        else:
            messages.error(request, 'Bad authentication. Please check your username and password.')
            return redirect('signin')

    return render(request, 'authentification/signin.html')


# def signout(request):
#     logout(request)
#     request.session.clear()
#     messages.success(request, 'logout successfully!')
#     return redirect('signin')    

def signout(request):
    # Redirection avant de supprimer les sessions
    redirect_url = 'signin'  
    logout(request)
    #messages.success(request, 'Logout successfully!')
    
    response = redirect(redirect_url)
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = 'Fri, 01 Jan 1990 00:00:00 GMT'
    
    return response



# usercrud

@login_required(login_url='signin')
def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

@login_required(login_url='signin')

def user_create(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']  
        role = request.POST['role']

        # Vérifier si l'utilisateur existe déjà
        if User.objects.filter(username=username).exists():
            #error_message = "Un utilisateur avec ce nom d'utilisateur existe déjà."
            messages.error(request, 'Un utilisateur avec ce nom d\'utilisateur existe déjà.')
            return render(request, 'user_create')


        user = User.objects.create_user(username=username, password=password, email=email)
        UserProfile.objects.create(user=user, role=role)
        return redirect('user_list')
    return render(request, 'users/user_create.html', {'roles': UserProfile._meta.get_field('role').choices})
@login_required(login_url='signin')

def user_update(request, user_id):
    user = User.objects.get(id=user_id)
    profile = UserProfile.objects.get(user=user)

    if request.method == 'POST':
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.save()
        profile.role = request.POST['role']
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

