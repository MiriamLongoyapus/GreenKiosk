from order.views import order_upload_view
from django.urls import path

urlpatterns = [
    path('order/upload/', order_upload_view, name='order_upload_view'),

]