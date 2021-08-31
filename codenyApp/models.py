from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils.translation import gettext as _
# Create your models here.

class Profile(models.Model):
    # atributes
    telefono = models.IntegerField(null=True)
    pais = models.TextField(max_length=30, null=False)
    # relation
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):  # show name in list admin
        return self.user.username

