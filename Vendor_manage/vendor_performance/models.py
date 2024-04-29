from django.db import models
from vendor_profile.models import vendor_profile

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(vendor_profile, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()


