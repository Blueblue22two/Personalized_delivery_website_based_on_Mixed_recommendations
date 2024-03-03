from django.urls import path

from . import views

urlpatterns = [
    # name 参数为 URL 模式提供了一个唯一的标识符
    path("", views.index, name="index"), # index page of log in
    # # login
    # path("login/customer/",views.login_customer,name="loginCustomer"),
    # path("login/merchant/",views.login_merchant,name="loginMerchant"),

    # register
    # path('customer/register/', views.customer_register, name='customer_register'),
    # path('merchant/register/', views.merchant_register, name='merchant_register'),
]
