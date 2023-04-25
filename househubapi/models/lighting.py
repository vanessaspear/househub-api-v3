from django.db import models
from .home_feature_area import HomeFeatureArea

class Lighting(models.Model):
    home_feature_area = models.ForeignKey(HomeFeatureArea, on_delete=CASCADE)
    lighting_usage_description = models.CharField(max_length=250)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    bulb_shape = models.CharField(max_length=100)
    wattage = models.FloatField()
    voltage = models.FloatField()
    lumens = models.FloatField()
    color_temperature = models.FloatField()
    color_description = models.CharField(max_length=150)
    lifespan = models.IntegerField()
    base_type = models.CharField(max_length=150)
    quantity = models.IntegerField()