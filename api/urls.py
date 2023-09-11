from django.urls import path
from .views import CustomerListView, CustomerDetailView, ProductListView, CartListView, OrderListView

urlpatterns = [
    path("customers/", CustomerListView.as_view(), name="customer_list_view"),
    path("customers/<int:id>/", CustomerDetailView.as_view(), name="customer_detail_view"),
    path("inventory/", ProductListView.as_view(), name="inventory_list_view"),
    path("cart/", CartListView.as_view(), name="cart_list_view"),
    path("order/", OrderListView.as_view(), name="order_list_view"),


]
