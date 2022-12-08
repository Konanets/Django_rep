from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators as V
from django.db import models

from .enums import RegEx
from .managers import UserManager
from .services import upload_avatar

# Create your models here.

class UserModel(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    crated_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    objects = UserManager()


class ProfileModel(models.Model):
    class Meta:
        db_table = 'profiles'

    name = models.CharField(max_length=15, validators=[V.RegexValidator(RegEx.NAME.pattern, RegEx.NAME.msg)])
    surname = models.CharField(max_length=20)
    age = models.IntegerField(validators=[V.MinValueValidator(18), V.MaxValueValidator(150)])
    phone = models.CharField(max_length=10)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to=upload_avatar, blank=False)
