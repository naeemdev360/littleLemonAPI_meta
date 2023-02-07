from rest_framework import serializers
from .models import MenuItem,FastFood,Category
from decimal import Decimal
import bleach

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','slug','title']

class MenuItemSerializer(serializers.ModelSerializer):
  stock = serializers.IntegerField(source='inventory')
  price_after_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')
  category_id = serializers.IntegerField(write_only=True)
  category = CategorySerializer(read_only=True)
  def validate_title(self,value):
     return bleach.clean(value)
  def validate_price(self,value):
        if (value < 2):
         raise serializers.ValidationError("Price should not be less than 2.0")
        return value
        
  class Meta:
   model = MenuItem
   fields = ['id','title','price','stock', 'price_after_tax','category','category_id']
   extra_kwargs = {
      'stock':{'source':'inventory','min_value':0}
   }
   
      
  def calculate_tax(self, product:MenuItem):
   return product.price * Decimal(1.1)
        

class FastFoodSerializer(serializers.ModelSerializer):
    cost = serializers.DecimalField(max_digits=6,decimal_places=2,source='price')
    price_after_tax= serializers.SerializerMethodField(method_name='calculate_tax')
    class Meta:
        model = FastFood
        fields = ['id','cost','name','price_after_tax']
    def calculate_tax(self,product:FastFood):
        return product.price * Decimal(1.1)