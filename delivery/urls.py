from delivery.views import delivery_upload_view
from django.urls import path

urlpatterns = [
    path('delivery/upload/', delivery_upload_view, name='delivery_upload_view'),

]