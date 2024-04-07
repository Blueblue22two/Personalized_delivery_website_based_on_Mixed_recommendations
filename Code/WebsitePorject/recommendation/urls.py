from django.urls import path
from . import views

urlpatterns = [
    # logout
    path('logout/', views.logout_view, name='logout'),

    # recommend
    path("get_recommend_dish/", views.get_recommend_dish, name="get_recommend_dish"),
    path("recommend_view/", views.all_recommend, name="all_recommend"),

    # most popular
    path("get_popular/", views.get_popular, name="get_popular"),
    path("popular_view/", views.all_popular, name="all_popular"),

    # most sales
    path("get_sales/", views.get_sales, name="get_sales"),
    path("sales_view/", views.all_sales, name="all_sales"),

    # search function
    path("get_search/", views.get_search, name="get_search"),

    # my favorite function
    path("get_favorite/", views.get_favorite, name="get_favorite"),
]