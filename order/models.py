from django.db import models
from customer.models import Customer
from cart.models import Cart
from delivery.models import Delivery




# Create your models here.
class Order(models.Model):
    customer = models.OneToOneField(Customer, null=True, on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart, null=True, on_delete=models.CASCADE)
    delivery=models.ManyToManyField(Delivery)
    order_number = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField()
    is_completed = models.BooleanField(default=False)