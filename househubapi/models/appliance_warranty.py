from django.db import models
from .appliance import Appliance

class ApplianceWarranty(models.Model):
    appliance = models.ForeignKey(Appliance, on_delete=models.CASCADE)
    warranty_type = models.CharField(null=True, blank=True, max_length=50)
    issuer = models.CharField(max_length=250)
    purchase_date = models.DateField(null=False)
    expiration_date = models.DateField(null=False)
    warranty_length = models.FloatField()
    purchase_price = models.FloatField(null=True, blank=True)
    warranty_documents = models.FileField(null=True, blank=True, upload_to='warranties/', max_length=250)
