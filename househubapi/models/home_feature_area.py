from django.db import models

class HomeFeatureArea(models.Model):

    feature_area = models.ForeignKey("FeatureArea", on_delete=models.CASCADE, related_name='home_feature_area')
    feature_zone = models.ForeignKey("FeatureZone", on_delete=models.CASCADE, related_name='home_feature_zone')
    home = models.ForeignKey("Home", on_delete=models.CASCADE,)
