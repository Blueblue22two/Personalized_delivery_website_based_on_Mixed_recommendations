from django.urls import path

from . import views

urlpatterns = [
    # user information page
    path('profile/', views.profile, name='profile'),

    # favorites
    path('fav/', views.fav, name='fav'),

]