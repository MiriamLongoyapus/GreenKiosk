# from rest_framework import serializers
# from customer.models import Customer
# from inventory.models import Product
# from order.models import Order
# from cart.models import Cart


# class CustomerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = '__all__'


# class ProductSerializer(serializers.ModelSerializer):
#     products = ProductSerializer(many=True)
#     class Meta:
#         model = Product
#         fields = '__all__'


# class CartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cart
#         fields = '__all__'


# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = '__all__'



from rest_framework import serializers
from customer.models import Customer
from inventory.models import Product
from order.models import Order
from cart.models import Cart

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
