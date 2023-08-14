from django.db import models

# Create your models here.

class Customer(models.Model):
    # user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    created_at = models 
