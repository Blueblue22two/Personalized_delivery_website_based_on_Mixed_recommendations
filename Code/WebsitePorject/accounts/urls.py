from django.urls import path
from . import views

urlpatterns = [
    # login
    path("login/customer/", views.login_customer, name="login_customer"),
    path("login/merchant/", views.login_merchant, name="login_merchant"),

    # register
    path('register/customer/', views.customer_register, name='customer_register'),
    path('register/merchant/', views.merchant_register, name='merchant_register'),

    # main page
    path('main/', views.main_page, name='main_page'),

    # session: get the session username and user type
    path('get_user_info/', views.get_user_info, name='get_user_info'),
    path('get_info/', views.get_info, name='get_info'),

    # logout
    path('logout/', views.logout_view, name='logout'),

    # Search
    path('search/', views.search, name='search'),
]