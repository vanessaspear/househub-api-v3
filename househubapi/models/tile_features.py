from django.db import models
from .flooring import Flooring

class TileFeatures(models.Model):
    flooring = models.ForeignKey(Flooring, on_delete=models.CASCADE)
    tile_material = models.CharField(null=True, blank=True, max_length=150)
    tile_color = models.CharField(null=True, blank=True, max_length=100)
    length = models.FloatField(null=True, blank=True, )
    width = models.FloatField(null=True, blank=True, )
    thickness = models.FloatField(null=True, blank=True, )
    grout_type = models.CharField(null=True, blank=True, max_length=150)
    grout_color =  models.CharField(null=True, blank=True, max_length=150)
    grout_make =  models.CharField(null=True, blank=True, max_length=150)
    grout_sealant =  models.CharField(null=True, blank=True, max_length=150)