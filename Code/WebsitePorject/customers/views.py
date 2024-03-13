from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from accounts.models import Customer

# Create your views here.

# user info page
def user_info(request):
    return render(request, 'base.html')

# TODO:增删修改address

