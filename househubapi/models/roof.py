from django.db import models
from .home_feature_area import HomeFeatureArea

class Roof(models.Model):
    home_feature_area = models.ForeignKey(HomeFeatureArea, on_delete=CASCADE)
    material = models.CharField(max_length=150)
    color = models.CharField(max_length=150)
    make = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    pitch = models.FloatField()
    weight = models.FloatField()
    lifespan = models.IntegerField(max=100)
    solar_reflectance_index = models.IntegerField(max=100)
    installation_method = models.CharField(max_length=250)