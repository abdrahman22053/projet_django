from django.db import models

class Users(models.Model):
    ROLE_CHOICES = [
        ('Directeur de l\'informatique', 'Directeur de l\'informatique'),
        ('Chef de réseau', 'Chef de réseau'),
        ('Chef de service', 'Chef de service')
    ]

    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    # profile = models.CharField(max_length=50, choices=ROLE_CHOICES, null=True, blank=True)

    def __str__(self):
        return f"{self.fname} {self.lname} - {self.profile}"
