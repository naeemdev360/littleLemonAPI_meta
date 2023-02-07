from django.urls import path
from . import views

urlpatterns = [
    path("menu-items",views.MenuItemsView.as_view()),
    path("menu-items/<int:pk>",views.SingleMenuItemView.as_view()),
    path("fast-food",views.FastFoodView.as_view()),
    path("fast-food/<int:pk>",views.SingleFastFood.as_view()),
    path('category',views.CategoryView.as_view()),
    path('category/<int:pk>',views.SingleCategoryView.as_view(),name='category-detail'),
]
