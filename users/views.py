from django.shortcuts import render, get_object_or_404, redirect
from .models import Users
from django.contrib.auth.decorators import login_required

@login_required(login_url='signin')
def users(request):
    users_list = Users.objects.all()
    return render(request, 'users/users.html', {'users_list': users_list})
@login_required(login_url='signin')

def add_user(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        profile = request.POST.get('profile')
        user = Users(fname=fname, lname=lname, profile=profile)
        user.save()
        return redirect('users')  # Redirect to the users list page
    return render(request, 'users/add_user.html')

def update_user(request, user_id):
    user = Users.objects.get(pk=user_id)
    if request.method == 'POST':
        user.fname = request.POST.get('fname')
        user.lname = request.POST.get('lname')
        user.profile = request.POST.get('profile')
        user.save()
        return redirect('users')  # Redirect to the users list page
    return render(request, 'users/update_user.html', {'user': user})

def delete_user(request, user_id):
    user = get_object_or_404(Users, pk=user_id)
    user.delete()
    return redirect('users')
