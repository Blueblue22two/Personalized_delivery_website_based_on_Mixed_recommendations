from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), # index page of log in
    path("loginc/",views.login_customer,name="loginc"), # login customer page
    path("loginm/",views.login_merchant,name="loginm"), # login merchant page
    path("registerc/",views.register_merchant,name="registerc"), # register customer page
    path("registerm/",views.register_merchant,name="registerm") # register merchant page
]