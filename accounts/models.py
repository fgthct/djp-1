from django.contrib.auth.models import AbstractUser
from django.db import models
import os

# Create your models here.
class CustomUser(AbstractUser):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('accounts', self.username, instance)
        return None

    STATUS = (
        ('Socio', 'Socio'),
        ('Sottoscrittore','Sottoscrittore'),
        ('Moderatore','Moderatore'),
    )

    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100, choices=STATUS, default='Sottoscrittore')
    description = models.TextField('Descrizione', max_length=600, default='', blank=True)
    image = models.ImageField(default='image_profile/user.jpg', upload_to='image_profile')

    def __str__(self):
        return self.username
    

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateField()

    def __str__(self):
        return str(self.user)