from django.contrib import admin
from.models import Vendor

# Register your models here.
class VendorAdmin(admin.ModelAdmin):
    list_display=("name","address","contact_number")
admin.site.register(Vendor, VendorAdmin)