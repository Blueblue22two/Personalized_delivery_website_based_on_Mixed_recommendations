from django.urls import path

from . import views

urlpatterns = [
    # user information page
    path('profile/', views.profile, name='profile'),

    # favorites
    path('fav/', views.fav, name='fav'),

    # add store to fav
    path('add_fav/',views.add_fav,name='add_fav'),

    # add product to fav
    path('add_fav_product/', views.add_fav_product, name='add_fav_product'),
]