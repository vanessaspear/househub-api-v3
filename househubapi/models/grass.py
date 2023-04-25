from django.db import models
from .home_feature_area import HomeFeatureArea

class Grass(models.Model):
    home_feature_area = models.ForeignKey(HomeFeatureArea, on_delete=CASCADE)
    type = models.CharField(max_length=150)

    