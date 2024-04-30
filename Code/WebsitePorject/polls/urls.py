from django.urls import path

from . import views

urlpatterns = [
    # default index page
    path("", views.index, name="index"),
    path("login/",views.login,name="login"),
    # not found/error
    path("error/",views.error_view,name="error_view"),
    # testing
    path("template/",views.template,name="template"),
]
