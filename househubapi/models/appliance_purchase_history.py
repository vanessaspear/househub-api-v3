from django.db import models
from .appliance import Appliance

class AppliancePurchaseHistory(models.Model):
    appliance = models.ForeignKey(Appliance, on_delete=CASCADE)
    purchase_date = models.DateField(null=True)
    place_of_purchase = models.CharField(max_length=250)
    purchase_price = models.FloatField()
    receipt = models.FileField(upload_to='receipts', max_length=250)