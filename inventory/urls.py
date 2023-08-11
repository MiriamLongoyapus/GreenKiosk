from django.urls import path 
from .views import product_upload
from .views import products_list
from .views import product_detail_view

urlpatterns = [
    path("products/upload/", product_upload, name="product_upload"),
    path("products/list/", products_list, name="products_list"),
    path("products/<int:id>", product_detail_view, name="product_details")
]