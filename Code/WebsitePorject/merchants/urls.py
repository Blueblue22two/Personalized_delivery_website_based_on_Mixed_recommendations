from django.urls import path
from . import views

urlpatterns = [
    # my store page
    path('my_store/', views.my_store, name='my_store'),

    # register a new store
    path('new/store/', views.new_store, name='new_store'),


    # product manage page
    path('mystore/manage', views.manage, name='manage'),
]