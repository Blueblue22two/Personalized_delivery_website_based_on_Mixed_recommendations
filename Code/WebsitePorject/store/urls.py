from django.urls import path
from . import views

urlpatterns = [
    # store page
    path('shop/<str:name>/', views.shop_view, name='shop_view'),
]