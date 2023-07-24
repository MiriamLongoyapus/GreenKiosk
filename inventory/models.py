from django.db import models

# Create your models here.
class Product(models.Model):
    price=models.DecimalField(max_digits=8,decimal_places=2)
    stock=models.PositiveBigIntegerField()
    image=models.ImageField()
    description=models.TextField()
    date_created=models.DateTimeField()
    date_updated=models.DateTimeField(auto_created=True)

def __str__(self):
    return self.price