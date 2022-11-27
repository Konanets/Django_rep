from django.db import models


# Create your models here.


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    mark = models.CharField(max_length=25)
    year = models.IntegerField()
    seats = models.IntegerField()
    body_type = models.CharField(max_length=20)
    engine_capacity = models.FloatField()
