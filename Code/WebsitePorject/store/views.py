from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from accounts.models import Customer, Merchant, Shop
from merchants.models import ShopRating, Product


# Create your views here.


# 用于生成点击跳转到商店页面的链接
def shop_view(request, name):
    shop = get_object_or_404(Shop, name=name)
    return render(request, 'store.html', {'shop': shop})


# get shop info in store page
def shop_info(request):
    if request.method == 'POST':
        shop_name = request.POST.get('shopName')

        try:
            # 根据商店名称查找商店
            shop = Shop.objects.get(name=shop_name)
            # 计算参与评分的人数
            ratings_count = ShopRating.objects.filter(shop=shop).count()
            # 将数据返回到前端
            print("get total rate successfully")
            return JsonResponse({'ratingsCount': ratings_count, 'success': True})
        except Shop.DoesNotExist:
            return JsonResponse({'error': 'Shop not found.'}, status=404)

    return JsonResponse({'error': 'Invalid request method.'}, status=400)


# get all product of a store in store page
def product_info(request):
    if request.method == 'POST':
        print("product_info....")
        shop_name = request.POST.get('shopName')
        print(f"shop name: {shop_name}")
        try:
            shop = Shop.objects.get(name=shop_name)
            # 添加一项id
            products = list(Product.objects.filter(shop=shop).values('id','name', 'price', 'category', 'image_path'))
            product_list = list(products)
            print("product list:")
            print(product_list)
            print("get product info successfully")
            return JsonResponse(products, safe=False)
        except ObjectDoesNotExist:
            print("Shop not found")
            return JsonResponse({'error': 'Shop not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)


def category_info(request):
    if request.method == 'POST':
        print("category_info....")
        shop_name = request.POST.get('shopName')
        print(f"shop name: {shop_name}")
        try:
            shop = Shop.objects.get(name=shop_name)
            categories = Product.objects.filter(shop=shop).values_list('category', flat=True).distinct()
            category_list = list(categories)
            print("Categories list:")
            print(category_list)
            print("get category successfully")
            return JsonResponse(category_list, safe=False)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Shop not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)


