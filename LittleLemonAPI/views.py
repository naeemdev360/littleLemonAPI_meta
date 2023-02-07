from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.decorators import api_view
from .models import MenuItem,FastFood,Category
from django.core.paginator import Paginator,EmptyPage
from .serializers import MenuItemSerializer,FastFoodSerializer,CategorySerializer

# views using function
@api_view(['GET',"POST"])
def menu_items(request):
    if request.method == 'GET':
        items = MenuItem.objects.select_related("category").all()
        category_name = request.query_params.get("category")
        to_price = request.query_params.get("to_price")
        search = request.query_params.get("search")
        ordering = request.query_params.get("ordering")
        perpage = request.query_params.get("perpage",default=2)
        page = request.query_params.get('page',default=1)
        if ordering:
            ordering_list = ordering.split(",")
            items = items.order_by(*ordering_list)
        if search:
            items = items.filter(title__startswith=search)
        if category_name:
            items = items.filter(category__title=category_name)
        if to_price:
            items = items.filter(price__lte=to_price)
        paginator = Paginator(items,per_page=perpage)
        try:
            items = paginator.page(number=page)
        except EmptyPage:
            items = []
        serialize_item = MenuItemSerializer(items,many=True)
        return Response(serialize_item.data)
    elif request.method == 'POST':
        serialize_item = MenuItemSerializer(data=request.data)
        serialize_item.is_valid(raise_exception=True)
        serialize_item.save()
        return Response(serialize_item.validated_data,HTTP_201_CREATED)

# Create your views here using generics
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

