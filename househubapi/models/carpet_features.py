from django.db import models
from .flooring import Flooring

class CarpetFeatures(models.Model):
    flooring = models.ForeignKey(Flooring, on_delete=CASCADE)
    material = models.CharField(max_length=150)
    padding = models.CharField(max_length=100)
    length = models.FloatField()
    width = models.FloatField()
    pile_height = models.FloatField()
    color = models.CharField(max_length=150)
    installation_method =  models.CharField(max_length=150)