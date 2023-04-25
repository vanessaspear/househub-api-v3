from django.db import models
from .flooring import Flooring

class HardwoodFeatures(models.Model):
    flooring = models.ForeignKey(Flooring, on_delete=CASCADE)
    material = models.CharField(max_length=150)
    finish = models.CharField(max_length=100)
    width = models.FloatField()
    length = models.FloatField()
    thickness = models.FloatField()
    hardness = models.FloatField()
    color = models.CharField(max_length=150)
    grade = models.CharField(max_length=150)
    installation_method =  models.CharField(max_length=150)