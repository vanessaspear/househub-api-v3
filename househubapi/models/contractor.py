from django.db import models
from django.contrib.auth.models import User

class Contractor(models.Model):
    
    phone = models.CharField(max_length=14)
    company = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_info')

