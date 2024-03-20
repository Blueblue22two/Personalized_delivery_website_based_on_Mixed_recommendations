from django.urls import path
from . import views

urlpatterns = [
    path('product_view/<int:product_id>/', views.product_view, name='product_view'),

    # get comment
    path('get_comment/', views.get_comment, name='get_comment'),
]