from django.db import models
from .home_feature_area import HomeFeatureArea

class Pool(models.Model):
    home_feature_area = models.ForeignKey(HomeFeatureArea, on_delete=CASCADE)
    length = models.FloatField()
    width = models.FloatField()
    depth = models.FloatField()
    shape = models.CharField(max_length=150)
    material = models.CharField(max_length=150)
    heating_system = models.CharField(max_length=250)
    filtration_system = models.CharField(max_length=100)
    lighting = models.CharField(max_length=100)
    water_type = models.CharField(max_length=100)
    