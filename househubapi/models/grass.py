from django.db import models
from .home_feature_area import HomeFeatureArea

class Grass(models.Model):
    home_feature_area = models.ForeignKey(HomeFeatureArea, on_delete=models.CASCADE)
    type = models.CharField(null=True, blank=True, max_length=150)

    