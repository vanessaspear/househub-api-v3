from django.db import models

class Appliance(models.Model):
    
    make = models.CharField(max_length=50)
    model = models.CharField(null=True, blank=True, max_length=50)
    serial_number = models.CharField(null=True, blank=True, max_length=50)
    year_built = models.PositiveIntegerField(null=True, blank=True)
    owners_manual = models.FileField(null=True, blank=True, upload_to='manuals/')
    appliance_type = models.ForeignKey("ApplianceType", on_delete=models.CASCADE, related_name='type_of_appliance')
    home_feature_area = models.ForeignKey("HomeFeatureArea", on_delete=models.CASCADE, related_name='appliance_in_area')



