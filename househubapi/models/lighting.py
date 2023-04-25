from django.db import models
from .home_feature_area import HomeFeatureArea

class Lighting(models.Model):
    home_feature_area = models.ForeignKey(HomeFeatureArea, on_delete=models.CASCADE)
    lighting_usage_description = models.CharField(null=True, blank=True, max_length=250)
    make = models.CharField(null=True, blank=True, max_length=100)
    model = models.CharField(null=True, blank=True, max_length=100)
    bulb_shape = models.CharField(null=True, blank=True, max_length=100)
    wattage = models.FloatField(null=True, blank=True, )
    voltage = models.FloatField(null=True, blank=True, )
    lumens = models.FloatField(null=True, blank=True, )
    color_temperature = models.FloatField(null=True, blank=True, )
    color_description = models.CharField(null=True, blank=True, max_length=150)
    lifespan = models.IntegerField(null=True, blank=True, )
    base_type = models.CharField(null=True, blank=True, max_length=150)
    quantity = models.IntegerField(null=True, blank=True, )