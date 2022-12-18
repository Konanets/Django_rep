from django.db import models

from apps.auto_parks.models import AutoParksModel

from .services import upload_photo

# Create your models here.


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    price = models.IntegerField()
    mark = models.CharField(max_length=25)
    year = models.IntegerField()
    seats = models.IntegerField()
    body_type = models.CharField(max_length=20)
    engine_capacity = models.FloatField()
    auto_park = models.ForeignKey(AutoParksModel, on_delete=models.CASCADE, related_name='cars')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class CarsPhotoModel(models.Model):
    class Meta:
        db_table = 'cars_photo'

    photo = models.ImageField(upload_to=upload_photo)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='photos')
