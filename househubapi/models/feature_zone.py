from django.db import models

class FeatureZone(models.Model):
    
    zone = models.CharField(max_length=50)
    