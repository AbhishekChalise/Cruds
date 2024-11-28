from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Main_User_Model(models.Model):
    user = models.OneToOneField(User , on_delete = models.CASCADE)
    is_Student = models.BooleanField()
    is_teacher = models.BooleanField()

    class Meta:
        pass

    def __str__(self):
        return f'{self.user.username}'



