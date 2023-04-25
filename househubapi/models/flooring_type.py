from django.db import models

class FlooringType(models.Model):
    type = models.CharField(max_length=100)