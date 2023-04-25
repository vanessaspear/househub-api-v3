from django.db import models
from django.core.validators import MinValueValidator

class UtilityProvider(models.Model):
    
    company = models.CharField(max_length=50)
    street = models.CharField(null=True, blank=True, max_length=50)
    city = models.CharField(null=True, blank=True, max_length=50)
    state = models.CharField(null=True, blank=True, max_length=50)
    email = models.CharField(null=True, blank=True, max_length=50)
    phone = models.CharField(null=True, blank=True, max_length=14)
    account_identifier = models.CharField(null=True, blank=True, max_length=100)
    plan_name = models.CharField(null=True, blank=True, max_length=100)
    cost_per_month = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0.0)])
    utility = models.ForeignKey("Utility", on_delete=models.CASCADE, related_name='utility_service')
    home = models.ForeignKey("Home", on_delete=models.CASCADE, related_name='home_utilities')


