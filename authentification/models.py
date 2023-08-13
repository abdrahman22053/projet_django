from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

class UserProfile(models.Model):
    x = (
        ('Chef de service', 'Chef de service'),
        ('Directeur de l\'informatique', 'Directeur de l\'informatique'),
        ('Chef réseau', 'Chef réseau')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices= x)


    def __str__(self):
        return f"{self.user.username} - {self.role}"