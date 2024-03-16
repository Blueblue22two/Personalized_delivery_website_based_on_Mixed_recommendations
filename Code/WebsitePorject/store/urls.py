from django.urls import path
from . import views

urlpatterns = [
    # store page
    path('store/<int:shop_id>/', views.store_page, name='store_page'),
]