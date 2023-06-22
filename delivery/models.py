from django.db import models

# Create your models here.
class Delivery(models.Model):
    delivery_status = models.CharField(max_length=255)
    tracking_number = models.CharField(max_length=255)
    delivery_date = models.DateField()
