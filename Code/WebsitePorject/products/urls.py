from django.urls import path
from . import views

urlpatterns = [
    # produce page
    path('product_view/<int:product_id>/', views.product_view, name='product_view'),

    # product category
    path('product_category/<str:category_name>/', views.product_category, name='product_category'),

    # get product category info
    path('category_info/', views.category_info, name='category_info'),

    # get comment
    path('get_comment/', views.get_comment, name='get_comment'),
]