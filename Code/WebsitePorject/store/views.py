from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from accounts.models import Customer, Merchant, Shop


# Create your views here.


# <!-- shops.html -->
# {% for shop in shops %}
#     <a href="{% url 'shop_view' name=shop.name %}">{{ shop.name }}</a><br>
# {% endfor %}

# 用于生成点击跳转到商店页面的链接
def shop_view(request):
    shops = Shop.objects.all()
    return render(request, 'shops.html', {'shops': shops})