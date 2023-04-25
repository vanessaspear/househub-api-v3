from django.db import models
from django.contrib.auth.models import User

class Household(models.Model):
    
    primary = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_info')
    home = models.ForeignKey("Home", on_delete=models.DO_NOTHING,)
    