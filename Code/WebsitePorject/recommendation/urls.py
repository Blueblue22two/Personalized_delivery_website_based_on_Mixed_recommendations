from django.urls import path
from . import views

urlpatterns = [
    # logout
    path('logout/', views.logout_view, name='logout'),

    # recommend
    path("get_recommend/", views.get_recommend, name="get_recommend"),

    # most popular
    path("get_popular/", views.get_popular, name="get_popular"),

    # most sales
    path("get_sales/", views.get_sales, name="get_sales"),
]