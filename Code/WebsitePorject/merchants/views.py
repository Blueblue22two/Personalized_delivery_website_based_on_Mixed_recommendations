from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from accounts.models import Merchant,Shop

# Create your views here.

# -- My store --
def myStore(request):
    # TODO: get cookie值username与user_type
    print("get cookie")
    # TODO:先检测merchant是否在store表格中已经注册，若已注册则返回商店界面
    # TODO: 若未注册则跳转到商店注册界面
    return