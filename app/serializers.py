from rest_framework import serializers
from .models import Item, OrderItem, Order
from django.contrib.auth.models import User

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'price']


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['item', 'quantity', 'order']

class OrderSerializer(serializers.ModelSerializer):
    total_amount = serializers.DecimalField(required=False, max_digits=10, decimal_places=2)
    # user = serializers.PrimaryKeyRelatedField(required=False, queryset=User.objects.all())  # Assuming User model is imported

    class Meta:
        model = Order
        fields = ['id', 'user', 'items', 'total_amount', 'is_paid', 'status']

