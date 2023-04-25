from django.db import models
from .home_feature_area import HomeFeatureArea

class FireExtinguisher(models.Model):
    home_feature_area = models.ForeignKey(HomeFeatureArea, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    location_in_area = models.CharField(null=True, blank=True, max_length=250)
    classification = models.CharField(null=True, blank=True, max_length=250)
    size = models.FloatField(null=True, blank=True, )
    extinguishing_agent = models.CharField(null=True, blank=True, max_length=250)
    range = models.FloatField(null=True, blank=True, )
    discharge_time = models.FloatField(null=True, blank=True, )
    certification = models.CharField(null=True, blank=True, max_length=100)
