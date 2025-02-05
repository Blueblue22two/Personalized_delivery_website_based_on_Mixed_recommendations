from django.urls import path
from . import views

urlpatterns = [
    # my store page
    path('my_store/', views.my_store, name='my_store'),

    # register a new store
    path('new/store/', views.new_store, name='new_store'),

    # upload shop rate
    path('upload_rate/', views.upload_rate, name='upload_rate'),

    # my store information
    path('my_store/get_info', views.get_info, name='get_info'),

    # product management
    path('my_store/add_product', views.add_product, name='add_product'),
    path('my_store/modify_product/', views.modify_product, name='modify_product'),
    path('my_store/delete_product/', views.delete_product, name='delete_product'),
    path('my_store/show_product/', views.show_product, name='show_product'),
]