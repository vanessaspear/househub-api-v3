from django.db import models
from .home_feature_area import HomeFeatureArea

class SmokeDetector(models.Model):
    home_feature_area = models.ForeignKey(HomeFeatureAreaa, on_delete=CASCADE)
    quantity = models.IntegerField()
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    power_source = models.CharField(max_length=200)
    date_installed = models.DateField()
    expiration_date = models.DateField()
    lifespan = models.IntegerField()
    carbon_monoxide_detector = models.BooleanField(null=False)
    manual = models.FileField(upload_to='manuals')