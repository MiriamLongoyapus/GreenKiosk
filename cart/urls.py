from django.urls import path
from .views import product_upload_view, cart_list, add_to_cart

urlpatterns= [
    path("products/get/", product_upload_view,name="product_get_view"),
    path('cart/add_to_cart/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_list, name='cart_list'),
]