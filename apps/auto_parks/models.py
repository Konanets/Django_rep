from django.db import models

from apps.users.models import UserModel


# Create your models here.
class AutoParksModel(models.Model):
    class Meta:
        db_table = 'auto_parks'

    name = models.CharField(max_length=35)
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='auto_parks')
