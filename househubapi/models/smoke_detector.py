from django.db import models
from .home_feature_area import HomeFeatureArea

class SmokeDetector(models.Model):
    home_feature_area = models.ForeignKey(HomeFeatureArea, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True, )
    make = models.CharField(null=True, blank=True, max_length=200)
    model = models.CharField(null=True, blank=True, max_length=200)
    type = models.CharField(null=True, blank=True, max_length=200)
    power_source = models.CharField(null=True, blank=True, max_length=200)
    date_installed = models.DateField(null=True, blank=True, )
    expiration_date = models.DateField(null=True, blank=True, )
    lifespan = models.IntegerField(null=True, blank=True, )
    carbon_monoxide_detector = models.BooleanField(null=False)
    manual = models.FileField(null=True, blank=True, upload_to='manuals')