from django.db import models

class ContractorSpecialty(models.Model):

    contractor = models.ForeignKey("Contractor", on_delete=models.CASCADE, related_name='contractor_info')
    specialty = models.ForeignKey("Specialty", on_delete=models.CASCADE, related_name='specialty_info')