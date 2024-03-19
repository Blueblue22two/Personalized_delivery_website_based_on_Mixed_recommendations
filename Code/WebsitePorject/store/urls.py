from django.urls import path
from . import views

urlpatterns = [
    # store page
    path('shop/<str:name>/', views.shop_view, name='shop_view'),
    # get shop info
    path('shop_info/', views.shop_info, name='shop_info'),
    # get product info
    path('product_info/', views.product_info, name='shop_info'),
    # get product info
    path('category_info/', views.category_info, name='category_info'),
]