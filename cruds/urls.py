from django.urls import path
from cruds import views

urlpatterns = [
    #path('list', views.list, name='list'),
    path('file_list/', views.file_list, name='file_list'),
    path('upload/', views.upload_file, name='upload_file'),
    path('delete_file/<int:pk>/', views.delete_file, name='delete_file'),
]