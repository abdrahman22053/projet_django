from django.urls import path
from authentification import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),



    # Users 
    path('list/', views.user_list, name='user_list'),
    path('create/', views.user_create, name='user_create'),
    path('update/<int:user_id>/', views.user_update, name='user_update'),
    path('delete/<int:user_id>/', views.user_delete, name='user_delete'),
]

