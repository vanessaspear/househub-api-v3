from django.db import models
from .flooring_type import FlooringType
from .home_feature_area import HomeFeatureArea

class Flooring(models.Model):
    make = models.CharField(null=True, blank=True, max_length=150)
    model = models.CharField(null=True, blank=True, max_length=150)
    year = models.DateField(null=True)
    flooring_type = models.ForeignKey(FlooringType, on_delete=models.CASCADE)
    home_feature_area = models.ForeignKey(HomeFeatureArea, on_delete=models.CASCADE)