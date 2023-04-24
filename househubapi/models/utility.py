from django.db import models

class Utility(models.Model):
    
    type = models.CharField(max_length=50)
    