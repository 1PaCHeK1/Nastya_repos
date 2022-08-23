from pyexpat import model
from rest_framework.serializers import ModelSerializer, Serializer

from .models import (
    Order,
    Product
)


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'type']


class OrderSerializer(ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Order
        fields = ['id', 'user', 'products', 'created_at', 'status', 'total_price']


class OrderCreateSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'products']
        read_only_fields = ['user', 'status']