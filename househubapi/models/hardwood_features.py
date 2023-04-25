from django.db import models
from .flooring import Flooring

class HardwoodFeatures(models.Model):
    flooring = models.ForeignKey(Flooring, on_delete=models.CASCADE)
    material = models.CharField(null=True, blank=True, max_length=150)
    finish = models.CharField(null=True, blank=True, max_length=100)
    width = models.FloatField(null=True, blank=True, )
    length = models.FloatField(null=True, blank=True, )
    thickness = models.FloatField(null=True, blank=True, )
    hardness = models.FloatField(null=True, blank=True, )
    color = models.CharField(null=True, blank=True, max_length=150)
    grade = models.CharField(null=True, blank=True, max_length=150)
    installation_method =  models.CharField(null=True, blank=True, max_length=150)