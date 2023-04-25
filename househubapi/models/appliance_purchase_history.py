from django.db import models
from .appliance import Appliance

class AppliancePurchaseHistory(models.Model):
    appliance = models.ForeignKey(Appliance, on_delete=models.CASCADE)
    purchase_date = models.DateField(null=True, blank=True)
    place_of_purchase = models.CharField(null=True, blank=True, max_length=250)
    purchase_price = models.FloatField(null=True, blank=True)
    receipt = models.FileField(null=True, blank=True, upload_to='receipts/', max_length=250)