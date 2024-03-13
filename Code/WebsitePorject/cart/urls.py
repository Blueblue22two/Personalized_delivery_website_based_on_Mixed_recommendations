from django.urls import path
from . import views

urlpatterns = [
    # main page
    path('main/', views.main_page, name='main_page'),
]