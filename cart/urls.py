from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...
    path('cart-upload/', views.cart_upload_view, name='cart_upload_view'),
   
]
