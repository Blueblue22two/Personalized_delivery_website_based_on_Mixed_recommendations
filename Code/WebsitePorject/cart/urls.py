from django.urls import path
from . import views

urlpatterns = [
    # shopping cart page
    path('main/', views.main_page, name='main_page'),

    # upload cart information & pay
    path('cart_info/', views.cart_info, name='cart_info'),

    # upload cart item form store page
    path('upload_cart/', views.upload_cart, name='upload_cart'),
    # upload cart item form cart page
    path('upload/', views.upload, name='upload'),

    # get a cart item of a store
    path('get_cart_store/', views.get_cart_store, name='get_cart_store'),

    # get all the cart item of a customer
    path('get_cart/', views.get_cart, name='get_cart'),
]