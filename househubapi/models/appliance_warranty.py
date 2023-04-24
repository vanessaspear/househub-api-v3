from django.db import models
from .appliance import Appliance

class ApplianceWarranty(models.Model):
    appliance = models.ForeignKey(Appliance, on_delete=CASCADE)
    warranty_type = models.CharField(max_length=50)
    issuer = models.CharField(max_length=250)
    purchase_date = models.DateField(null=False)
    expiration_date = models.DateField(null=False)
    warranty_length = models.FloatField()
    purchase_price = models.FloatField()
    warranty_documents = models.FileField(upload_to='warranties', max_length=250)
