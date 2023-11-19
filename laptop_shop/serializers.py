from rest_framework import serializers
from .models import AppleStore
from .models import Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppleStore
        fields = 'id title created_at'.split()


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppleStore
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['product', 'quantity']

    def create(self, validated_data):
        return Order.objects.create(**validated_data)
