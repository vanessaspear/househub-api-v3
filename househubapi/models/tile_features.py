from django.db import models
from .flooring import Flooring

class TileFeatures(models.Model):
    flooring = models.ForeignKey(Flooring, on_delete=CASCADE)
    tile_material = models.CharField(max_length=150)
    tile_color = models.CharField(max_length=100)
    length = models.FloatField()
    width = models.FloatField()
    thickness = models.FloatField()
    grout_type = models.CharField(max_length=150)
    grout_color =  models.CharField(max_length=150)
    grout_make =  models.CharField(max_length=150)
    grout_sealant =  models.CharField(max_length=150)