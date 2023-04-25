from django.db import models
from .home_feature_area import HomeFeatureArea

class Paint(models.Model):
    home_feature_area = models.ForeignKey(HomeFeatureArea, on_delete=CASCADE)
    paint_usage_description = models.CharField(max=250)
    make = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    finish = models.CharField(max_length=150)
    make = models.CharField(max_length=150)
    coverage = models.CharField(max_length=150)
    VOC_content = models.CharField(max_length=150)
    durability = models.CharField(max_length=150)
    color_retention = models.CharField(max_length=150)