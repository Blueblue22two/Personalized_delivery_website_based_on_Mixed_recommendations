from django.urls import path

from . import views

urlpatterns = [
    # user information page
    path('info/', views.user_info, name='user_info'),
]