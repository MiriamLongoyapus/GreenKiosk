# from django.db import models
# from customer.models import Customer
# from cart.models import Cart
# from delivery.models import Delivery
# from order.models import Order






# # Create your models here.
# class Order(models.Model):
#     customer = models.OneToOneField(Customer, null=True, on_delete=models.CASCADE)
#     cart=models.ForeignKey(Cart, null=True, on_delete=models.CASCADE)
#     delivery=models.ManyToManyField(Delivery)
#     order_number = models.CharField(max_length=50)
#     customer_name = models.CharField(max_length=100)
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     order_date = models.DateField()
#     is_completed = models.BooleanField(default=False)


from django.db import models
from customer.models import Customer
from cart.models import Cart
from delivery.models import Delivery

class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, null=True, on_delete=models.CASCADE)
    deliveries = models.ManyToManyField(Delivery)
    order_number = models.CharField(max_length=50, unique=True)  # Assuming it's a unique identifier for orders
    customer_name = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.order_number} by {self.customer_name}"
