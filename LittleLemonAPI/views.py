from django.shortcuts import render
from rest_framework import generics
from .models import MenuItem,FastFood,Category
from .serializers import MenuItemSerializer,FastFoodSerializer,CategorySerializer

# Create your views here.
class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class SingleCategoryView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class  = MenuItemSerializer
class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class FastFoodView(generics.ListCreateAPIView):
    queryset = FastFood.objects.all()
    serializer_class = FastFoodSerializer

class SingleFastFood(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = FastFood.objects.all()
    serializer_class = FastFoodSerializer

