from django.db import models

from apps.users.models import UserModel


# Create your models here.
class AutoParksModel(models.Model):
    class Meta:
        db_table = 'auto_parks'

    name = models.CharField(max_length=35)
    owner = models.ManyToManyField(UserModel, through='AutoParksUsersModel', related_name='auto_parks')


class AutoParksUsersModel(models.Model):
    class Meta:
        db_table = 'auto_parks_users'

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    auto_park = models.ForeignKey(AutoParksModel, on_delete=models.CASCADE)
