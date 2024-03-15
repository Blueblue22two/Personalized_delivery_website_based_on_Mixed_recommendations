from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from accounts.models import Customer

# Create your views here.


# user profile page
def profile(request):
    return render(request, 'profile.html')


# user favorite
def fav(request):
    return render(request, 'fav.html')


# TODO:增删修改address

