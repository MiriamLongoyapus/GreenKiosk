from django.contrib import admin
from.models import Payment


# Register your models here.
class PaymentAdmin(admin.ModelAdmin):
    list_display=("payment_id","amount","payment_date","is_successful")
admin.site.register(Payment, PaymentAdmin)
