from django.urls import path

from . import views

urlpatterns = [
    # favorites page
    path('fav/', views.fav, name='fav'),
    # Cancel favorite
    path('cancel_product_fav/<int:id>/', views.cancel_product_fav, name='cancel_product_fav'),

    path('cancel_shop_fav/<str:name>/', views.cancel_shop_fav, name='cancel_shop_fav'),
    # add store to fav
    path('add_fav/',views.add_fav,name='add_fav'),

    # add product to fav
    path('add_fav_product/', views.add_fav_product, name='add_fav_product'),

    # add a new address
    path('add_address/', views.add_address, name='add_address'),

    # get all the address of this customer
    path('get_address/', views.get_address, name='get_address'),
]