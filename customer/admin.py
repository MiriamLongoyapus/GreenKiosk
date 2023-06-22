from django.contrib import admin
from.models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=("last_name","email","phone_number","created_at")
admin.site.register(Customer, CustomerAdmin)
