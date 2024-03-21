from django.urls import path

from . import views

urlpatterns = [
    # user information page
    path('profile/', views.profile, name='profile'),

    # favorites page
    path('fav/', views.fav, name='fav'),

    # add store to fav
    path('add_fav/',views.add_fav,name='add_fav'),

    # add product to fav
    path('add_fav_product/', views.add_fav_product, name='add_fav_product'),

    # add a new address
    path('add_address/', views.add_address, name='add_address'),

    # get all the address of this customer
    path('get_address/', views.get_address, name='get_address'),
]