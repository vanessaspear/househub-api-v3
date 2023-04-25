from django.db import models
from .home_feature_area import HomeFeatureArea

class Roof(models.Model):
    home_feature_area = models.ForeignKey(HomeFeatureArea, on_delete=models.CASCADE)
    material = models.CharField(null=True, blank=True, max_length=150)
    color = models.CharField(null=True, blank=True, max_length=150)
    make = models.CharField(null=True, blank=True, max_length=150)
    model = models.CharField(null=True, blank=True, max_length=150)
    pitch = models.FloatField(null=True, blank=True, )
    weight = models.FloatField(null=True, blank=True, )
    lifespan = models.IntegerField(null=True, blank=True)
    solar_reflectance_index = models.IntegerField(null=True, blank=True)
    installation_method = models.CharField(null=True, blank=True, max_length=250)