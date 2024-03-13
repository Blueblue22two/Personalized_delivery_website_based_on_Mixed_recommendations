from django.urls import path
from . import views

urlpatterns = [
    # my store page
    path('myStore/', views.myStore, name='myStore'),

    # product manage page
    path('mystore/manage', views.manage, name='manage'),
]