from django.contrib import admin
from.models import product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=("name","stock","price","date_created")
admin.site.register(product, ProductAdmin)
