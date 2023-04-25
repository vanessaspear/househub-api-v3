from django.db import models
from .home_feature_area import HomeFeatureArea

class Fence(models.Model):
    home_feature_area = models.ForeignKey(HomeFeatureArea, on_delete=CASCADE)
    width = models.FloatField()
    height = models.FloatField()
    style = models.CharField(max_length=150)
    material = models.CharField(max_length=150)
    paint_make = models.CharField(max_length=250)
    paint_model = models.CharField(max_length=100)
    paint_color = models.CharField(max_length=100)
    