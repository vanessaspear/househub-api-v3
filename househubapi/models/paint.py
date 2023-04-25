from django.db import models
from .home_feature_area import HomeFeatureArea

class Paint(models.Model):
    home_feature_area = models.ForeignKey(HomeFeatureArea, on_delete=models.CASCADE)
    paint_usage_description = models.CharField(null=True, blank=True, max_length=250)
    make = models.CharField(null=True, blank=True, max_length=150)
    model = models.CharField(null=True, blank=True, max_length=150)
    finish = models.CharField(null=True, blank=True, max_length=150)
    coverage = models.CharField(null=True, blank=True, max_length=150)
    VOC_content = models.CharField(null=True, blank=True, max_length=150)
    durability = models.CharField(null=True, blank=True, max_length=150)
    color_retention = models.CharField(null=True, blank=True, max_length=150)