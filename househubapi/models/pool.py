from django.db import models
from .home_feature_area import HomeFeatureArea

class Pool(models.Model):
    home_feature_area = models.ForeignKey(HomeFeatureArea, on_delete=models.CASCADE)
    length = models.FloatField(null=True, blank=True, )
    width = models.FloatField(null=True, blank=True, )
    depth = models.FloatField(null=True, blank=True, )
    shape = models.CharField(null=True, blank=True, max_length=150)
    material = models.CharField(null=True, blank=True, max_length=150)
    heating_system = models.CharField(null=True, blank=True, max_length=250)
    filtration_system = models.CharField(null=True, blank=True, max_length=100)
    lighting = models.CharField(null=True, blank=True, max_length=100)
    water_type = models.CharField(null=True, blank=True, max_length=100)
    