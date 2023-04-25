from django.db import models
from .home_feature_area import HomeFeatureArea

class FireExtinguisher(models.Model):
    home_feature_area = models.ForeignKey(HomeFeatureArea, on_delete=CASCADE)
    quantity = models.IntegerField(max=1000)
    location_in_area = models.CharField(max_length=250)
    classification = models.CharField(max_length=250)
    size = models.FloatField()
    extinguishing_agent = models.CharField(max_length=250)
    range = models.FloatField()
    discharge_time = models.FloatField()
    certification = models.CharField()
