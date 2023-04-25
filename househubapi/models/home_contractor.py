from django.db import models

class HomeContractor(models.Model):
    
    phone = models.CharField(max_length=14)
    email = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    POC_name = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    specialty = models.ForeignKey("Specialty", on_delete=models.DO_NOTHING, related_name='contractor_specialty')
    home = models.ForeignKey("Home", on_delete=models.DO_NOTHING, related_name='home_info')

