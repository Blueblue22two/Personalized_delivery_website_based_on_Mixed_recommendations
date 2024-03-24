from django.urls import path
from . import views

urlpatterns = [
    # my order page
    path("my_orders/", views.my_orders, name="my_orders"),

    # get order information
    path("get_order/", views.get_order, name="get_order"),

    # Send Order
    path("send_order/<int:id>/", views.send_order, name="send_order"),

    # Post a comment page
    path("post_comment_view/<int:id>/", views.post_comment_view, name="post_comment_view"),

    # get order info in comment page
    path("get_info/", views.get_info, name="get_info"),

    # Post a comment
    path("post_comment/", views.post_comment, name="post_comment"),
]