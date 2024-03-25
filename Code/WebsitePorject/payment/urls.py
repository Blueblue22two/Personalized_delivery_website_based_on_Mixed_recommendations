from django.urls import path
from . import views

urlpatterns = [
    # payment page and payment function
    path("payment_view/", views.payment_view, name="payment_view"),

    # get cart info and create payment
    path("generate_payment/", views.generate_payment, name="generate_payment"),

    # get session storage data
    path("get_order_storage/", views.get_order_storage, name="get_order_storage"),
]

