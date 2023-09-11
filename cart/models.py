from django.db import models
from inventory.models import Product


# Create your models here.
class Cart(models.Model):
    products = models.ManyToManyField(Product) 
    quantity= models.PositiveBigIntegerField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    shipping_price =  models.DecimalField(max_digits=6,decimal_places=2)
    Payment_method = models.CharField (max_length=32)
    image=models.ImageField()
    
    def add_products(self,product):
        self.product.add(product)
        self.save()
        return self
    
    def get_total(self):
        products = self.products
        total = 0
        for products in products:
            total += product.price
            return total


# total = sum([product.price for product in self.products])

# def __str__(self):
#     return f"Cart {self.pk}"
