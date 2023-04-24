from django.db import models

class AppliancePurchaseHistory(models.Model):
    appliance = models.ForeignKey(Appliance, on_delete=models.CASCADE)
    purchase_date = models.DateField(null = True)
    place_of_purchase = models.CharField(max_length=100)
    purchase_price  = models.FloatField()
    receipt = models.FileField(upload_to='receipts', max_length=354)