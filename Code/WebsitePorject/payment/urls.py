from django.urls import path
from . import views

urlpatterns = [
    # payment page, id= order id
    path("payment/", views.payment, name="payment"),

    # get cart info and create payment
    path("generate_payment/", views.generate_payment, name="generate_payment"),
]

