from rest_framework import serializers
from .models import MenuItem,FastFood,Category
from decimal import Decimal

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','slug','title']

class MenuItemSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    # category = serializers.RelatedField()
    class Meta:
        model = MenuItem
        fields = ['id','title','price','inventory','category']
        

class FastFoodSerializer(serializers.ModelSerializer):
    cost = serializers.DecimalField(max_digits=6,decimal_places=2,source='price')
    price_after_tax= serializers.SerializerMethodField(method_name='calculate_tax')
    class Meta:
        model = FastFood
        fields = ['id','cost','name','price_after_tax']
    def calculate_tax(self,product:FastFood):
        return product.price * Decimal(1.1)