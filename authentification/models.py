from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    ROLES = [
        ('Chef de service', 'Chef de service'),
        ('Directeur de l\'informatique', 'Directeur de l\'informatique'),
        ('Chef réseau', 'Chef réseau')
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=ROLES)
    chef = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subordinates')
    
    def __str__(self):
        return f"{self.user.username} - {self.role}"



class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
