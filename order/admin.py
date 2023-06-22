from django.contrib import admin
from.models import Order


# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display=("customer_name","total_amount","order_date","is_completed")
admin.site.register(Order, OrderAdmin)
