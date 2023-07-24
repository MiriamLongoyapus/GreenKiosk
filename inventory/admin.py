from django.contrib import admin
from inventory.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=("stock","price","date_created")
admin.site.register(Product, ProductAdmin)
