from django.contrib import admin
from.models import Delivery


# Register your models here.
class DeliveryAdmin(admin.ModelAdmin):
    list_display=("delivery_status","tracking_number")
admin.site.register(Delivery, DeliveryAdmin)
