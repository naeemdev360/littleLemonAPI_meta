from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("menu-items/",views.menu_items,name='menu-items'),
    path("menu-items/<int:pk>",views.SingleMenuItemView.as_view()),
    path("fast-food",views.FastFoodView.as_view()),
    path("fast-food/<int:pk>",views.SingleFastFood.as_view()),
    path('category',views.CategoryView.as_view()),
    path('category/<int:pk>',views.SingleCategoryView.as_view(),name='category-detail'),
    path('secret/',views.secret,name='secret'),
    path('api-token-auth/',obtain_auth_token),
]

