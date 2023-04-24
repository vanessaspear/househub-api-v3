from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Home(models.Model):
    
    name = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    bedrooms = models.PositiveIntegerField(null=True, blank=True)
    bathrooms = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0.0)])
    sq_footage = models.PositiveIntegerField(null=True, blank=True)
    lot_size = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0.0)])
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_info')

