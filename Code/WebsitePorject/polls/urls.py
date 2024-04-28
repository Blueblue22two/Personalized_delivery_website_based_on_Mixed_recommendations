from django.urls import path

from . import views

urlpatterns = [
    # default index page
    path("", views.index, name="index"),
    path("login/",views.login,name="login"),

    # testing
    path("template/",views.template,name="template"),
]
