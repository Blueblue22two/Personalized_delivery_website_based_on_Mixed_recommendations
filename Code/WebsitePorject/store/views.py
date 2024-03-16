from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from accounts.models import Customer, Merchant

# Create your views here.


def store_page(request):
# HTML展示
# < !-- 假设你在上下文中有一个名为shops的商店列表 -->
#     { %
#         for shop in shops %}
#         < div
#
#         class ="shop" >
#
#         < h2 > {{shop.name}} < / h2 >
#         < !-- 创建指向商店详细页面的链接 -->
#         < a
#         href = "{% url 'shop_detail' shop_id=shop.id %}" > Visit
#         {{shop.name}} < / a >
#
#         < / div >
#     { % endfor %}

# TODO:使用get_object_or_404快捷函数确保商店存在
    # shop = get_object_or_404(Shop, pk=shop_id)
    # return render(request, 'store.html', {'shop': shop})
    return