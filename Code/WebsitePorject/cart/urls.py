from django.urls import path
from . import views

urlpatterns = [
    # main page
    path('main/', views.main_page, name='main_page'),

    # upload cart information & pay
    path('cart_info/', views.cart_info, name='cart_info'),

    # upload
    path('upload_cart/', views.upload_cart, name='upload_cart'),
]