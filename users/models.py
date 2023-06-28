from django.contrib.auth.models import AbstractUser, User
from django.db import models
from catalog.models import NULLABLE
import random

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name = 'электронная почта')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to = 'users', verbose_name = 'аватар', **NULLABLE)
    country = models.CharField(verbose_name = 'Страна', **NULLABLE)

    token = models.CharField(max_length=200, verbose_name='токен', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время создания токена', **NULLABLE)
    #token_time = models.DateTimeField(auto_now_add=True, verbose_name='время создания токена', **NULLABLE)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     token = models.CharField(max_length=200)
#     is_verified = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)


