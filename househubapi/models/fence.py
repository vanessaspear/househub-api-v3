from django.db import models
from .home_feature_area import HomeFeatureArea

class Fence(models.Model):
    home_feature_area = models.ForeignKey(HomeFeatureArea, on_delete=models.CASCADE)
    width = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    style = models.CharField(null=True, blank=True, max_length=150)
    material = models.CharField(null=True, blank=True, max_length=150)
    finish_manufacturer = models.CharField(null=True, blank=True, max_length=250)
    finish_product = models.CharField(null=True, blank=True, max_length=100)
    finish_color = models.CharField(null=True, blank=True, max_length=100)
    