# coding: utf-8
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    pass

class User(AbstractBaseUser):
    cpf = models.CharField(max_length=11, unique=True, db_index=True)
    name = models.CharField(max_length=100, null=True)

    USERNAME_FIELD = 'cpf'

    objects = UserManager()
