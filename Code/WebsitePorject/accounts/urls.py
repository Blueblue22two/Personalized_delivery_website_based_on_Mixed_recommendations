from django.urls import path

from . import views

urlpatterns = [
    # login
    path("login/customer/", views.login_customer, name="login_customer"), # name用于模板中引用该特定的URL模式时，使用{% url 'customer_register' %}来引用
    path("login/merchant/", views.login_merchant, name="login_merchant"),

    # register
    path('accounts/register/customer/', views.customer_register, name='customer_register'),
    path('accounts/register/merchant/', views.merchant_register, name='merchant_register'),

    # log out

    # main page
    path('main/customer', views.customer_register, name='customer_register'),
]