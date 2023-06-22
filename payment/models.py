from django.db import models

# Create your models here.

class Payment(models.Model):
    payment_id = models.CharField(max_length=50, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField()
    is_successful = models.BooleanField(default=False)
