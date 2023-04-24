from django.db import models

class Specialty(models.Model):
    
    type = models.CharField(max_length=50)
    