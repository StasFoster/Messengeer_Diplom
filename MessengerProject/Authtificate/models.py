from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):

    

    class Meta:
        verbose_name = ("UserModel")
        verbose_name_plural = ("UserModels")

    def __str__(self):
        return self.name

