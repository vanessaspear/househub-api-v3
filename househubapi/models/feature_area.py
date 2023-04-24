from django.db import models

class FeatureArea(models.Model):
    
    area = models.CharField(max_length=50)
    