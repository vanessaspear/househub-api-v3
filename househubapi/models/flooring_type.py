from django.db import models

class FlooringType(models.Model):
    flooring_type = models.CharField(max_length=100)