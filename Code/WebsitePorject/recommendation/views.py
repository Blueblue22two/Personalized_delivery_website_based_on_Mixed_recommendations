from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from accounts.models import Customer, Merchant, Shop
from merchants.models import Product, ShopRating
from orders.models import Order


# Create your views here.


# -- logout(clear session) & redirect to main page--
def logout_view(request):
    print("log out...")
    logout(request)
    print("log out successfully,redirect to /")
    return HttpResponseRedirect('/')


# -- get the recommended store--
def get_recommend(request):
    # TODO:在数据库中查找recommend的商店信息并返回到前端
    # TODO: 待实现
    # TODO:
    # TODO: 推荐的排序
    # TODO:返回前6个商店的信息
    # TODO:返回的每个商店的数据信息包括: 1.total_rating 2.ShopRating中数据的数量 3.Shop的image_path 4.Shop的name 5.Shop的address
    return


# -- get the most popular store--
def get_popular(request):
    # 在数据库中查找的商店信息并返回到前端
    # TODO: 已知返回的每个商店的数据信息包括: 1.total_rating 2.变量popularity_value 3.Shop的image_path 4.Shop的name 5.Shop的address
    # 变量popularity_value:以一个shop为一个单位,对一个Shop表格中的一个商店，查找在ShopRating表格中对应的数据的数量,就是popularity_value
    # TODO: 先创建一种数据结构叫info包含以下的信息 1.total_rating(float) 2.popularity_value（int） 3.image_path(string) 4.name(string) 5.address(string)
    # TODO: 在Shop表格中先按照total_rating的数值从高到低排序，取排名前20的shop并都为其创造对应的数据结构info并按照顺序创建一个list来保存这些info
    # TODO: 对于list中的所有info，再按照下面的规则进行重新排序：
    # TODO: 对每个info取其total_rating与popularity_value按照 score = total_rating*0.6 + popularity_value*0.4的公式计算出每个info的score(score保留一位小数)
    # TODO: 对这个list中的info全部按照score的数值从大到小排序
    # TODO: 按照排序的顺序，仅返回list中前8个商店的info数据
    return


# -- get the most sales store--
# TODO:按照商店shop中所有product的销量之和 （商店的总销量）来排序
def get_sales(request):
    # 在数据库中查找的商店信息并返回到前端
    # TODO: 已知返回的每个商店的数据信息包括: 1.total_rating 2.变量popularity_value 3.Shop的image_path 4.Shop的name 5.Shop的address
    # 变量popularity_value:以一个shop为一个单位,对一个Shop表格中的一个商店，查找在ShopRating表格中对应的数据的数量,就是popularity_value
    # TODO: 先创建一种数据结构叫info包含以下的信息 1.total_rating(float) 2.popularity_value（int） 3.image_path(string) 4.name(string) 5.address(string)
    # TODO: 对于Shop表格中的每个商店，通过shop查找其在Merchant表格中的数据，再通过merchant来查找其在Order表格中所有对应的order(既在Order表格的一条数据)中的quantity
    # TODO: 将一个shop对应的一个merchant在Order表格中对应的所有数据中的quantity求和的值叫total_sale，
    # TODO: 创建另外一种数据结构叫Sales_info，该数据记录下面2种信息:1.shop的name 2.total_sale(int)
    # TODO: 创建一个list 未完成
    # TODO:返回前3个商店的信息

    return
