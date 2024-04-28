from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.hashers import make_password


# redirect to main page
def index(request):
    return render(request, 'main_index.html')


# redirect to login page of choose user type
def login(request):
    return render(request, 'login.html')


# test
def template(request):
    psw1 = '11111111'
    psw2 = '99999999'

    # hash password
    password1 = make_password(psw1)
    print("Hash Password1:", password1)
    password2 = make_password(psw2)
    print("Hash Password2:", password2)
