from django.db import models

class ApplianceType(models.Model):
    
    type = models.CharField(max_length=50)
    