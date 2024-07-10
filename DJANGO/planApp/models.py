from django.db import models
from django.utils import timezone

# Create your models here.
class SoilMoistureReading(models.Model):
    timestamp=models.DateTimeField(default=timezone.now)
    soil_level=models.FloatField()

    def _str_(self):
        return f"{self.timestamp}-{self.soil_level}"