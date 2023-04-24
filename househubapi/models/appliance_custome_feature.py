from django.db import models

class ApplianceCustomFeature(models.Model):
    custom_feature = models.CharField(max_length=50)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50)
    length = models.FloatField(null=True, blank=True)
    width = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    size = models.FloatField(null=True, blank=True)
    volume = models.FloatField(null=True, blank=True)
    appliance = models.ForeignKey("Appliance", on_delete=models.CASCADE, related_name='appliance_custom_features')
    