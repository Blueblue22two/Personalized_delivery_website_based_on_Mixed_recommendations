from django.urls import path
from . import views

urlpatterns = [
    # main page
    path('main/', views.main_page, name='main_page'),

    # upload cart information & pay
    path('get_cart_info/', views.get_cart_info, name='get_cart_info'),
]