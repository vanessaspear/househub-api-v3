from django.db import models
from .flooring import Flooring

class CarpetFeatures(models.Model):
    flooring = models.ForeignKey(Flooring, on_delete=models.CASCADE)
    material = models.CharField(null=True, blank=True, max_length=150)
    padding = models.CharField(null=True, blank=True, max_length=100)
    length = models.FloatField(null=True, blank=True, )
    width = models.FloatField(null=True, blank=True, )
    pile_height = models.FloatField(null=True, blank=True, )
    color = models.CharField(null=True, blank=True, max_length=150)
    installation_method =  models.CharField(null=True, blank=True, max_length=150)