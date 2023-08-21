from django.urls import path 
from .views import product_upload,product_list,product_detail_view, product_update_view

urlpatterns = [
    path("product/upload/", product_upload, name="product_upload"),
    path("product/list/", product_list, name="product_list"),
    path("product/<int:id>", product_detail_view, name="product_detail_view"),
    path("product/edit/<int:id>/", product_update_view, name='product_update_view')
]