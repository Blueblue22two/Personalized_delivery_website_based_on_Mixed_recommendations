from django.urls import path
from . import views

urlpatterns = [
    # my orders
    path("my_orders/", views.my_orders, name="my_orders"),
]