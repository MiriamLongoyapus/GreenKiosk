from .views import customer_upload, customer_list, customer_detail_view,edit_customer_view
from django.urls import path

urlpatterns = [
    path("customer/upload", customer_upload,name="customer_upload"),
    path("customer/list/", customer_list, name="customer_list"),
    path("customer/<int:id>", customer_detail_view, name="customer_detail_view"),
    path("customer/edit/<int:id>/", edit_customer_view, name='edit_customer_view'),

]