from django.urls import path
from users import views


urlpatterns = [
    path('users', views.users, name='users'),
    path('add_user', views.add_user, name='add_user'),
    path('update_user/<int:user_id>/', views.update_user, name='update_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
]