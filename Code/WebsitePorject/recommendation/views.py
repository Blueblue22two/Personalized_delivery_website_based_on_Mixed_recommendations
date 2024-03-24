import csv
import os
from django.shortcuts import render
from django.db.models import Count, Sum
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth import logout
from decimal import Decimal
from django.conf import settings
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
    # TODO: 推荐的排序
    # TODO:返回前6个商店的信息
    # TODO:返回的每个商店的数据信息包括: 1.total_rating 2.ShopRating中数据的数量 3.Shop的image_path 4.Shop的name 5.Shop的address
    # TODO: csv文件中的数据1.total_rating(float) 2.popularity_value（int） 3.image_path(string) 4.name(string) 5.address(string) 6. score(float)
    # 此时先模仿popular的数据，直接从popular.csv中存储的数据中读取前6位的shop的数据然后返回到前端
    dataset_base_dir = os.path.join(settings.BASE_DIR, 'Dataset')
    csv_file_path = os.path.join(dataset_base_dir, 'popular.csv')

    shops = []
    try:
        with open(csv_file_path, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            # 读取前6个商店信息
            for i, row in enumerate(reader):
                if i < 6:
                    shops.append(row)
                else:
                    break
    except FileNotFoundError:
        return JsonResponse({'error': 'File not found'}, status=404)

    return JsonResponse(shops, safe=False)


# -- get the most popular store--
def get_popular(request):
    # 在数据库中查找的商店信息并返回到前端
    # TODO: 创建一个csv文件叫popular.csv位于dataset_base_dir = os.path.join(settings.BASE_DIR, 'Dataset')中
    # TODO: 若该csv文件已存在,则重新覆盖该文件
    # TODO: csv文件中的数据1.total_rating(float) 2.popularity_value（int） 3.image_path(string) 4.name(string) 5.address(string) 6. score(float)
    # TODO: 以一个shop为单位，在Shop表格中先按照total_rating的数值从高到低排序，取排名前24的shop的total_rating, image_path ,name, address先存入该csv文件中
    # 对于popularity_value的值，是以每一个shop为单位，获取其对应ShopRating表格中对应的数据的数量。获取完毕后，再将其存入csv文件中对应的数据中
    # TODO: 然后对csv中每条数据，取其total_rating与popularity_value按照 score = total_rating*0.6 + popularity_value*0.4的公式计算出score(score保留一位小数)
    # TODO: 对这个csv文件按照score的数值从大到小重新排序
    # TODO: 按照排序的顺序，仅返回csv中排名前8的所有数据
    dataset_base_dir = os.path.join(settings.BASE_DIR, 'Dataset')
    if not os.path.exists(dataset_base_dir):
        os.makedirs(dataset_base_dir)

    csv_file_path = os.path.join(dataset_base_dir, 'popular.csv')
    print(f"popular.cv path: {csv_file_path}")

    # Fetch top 24 shops based on total_rating
    top_shops = Shop.objects.annotate(popularity_value=Count('ratings')).order_by('-total_rating')[:24]

    # Prepare CSV data
    with open(csv_file_path, 'w', newline='') as csvfile:
        fieldnames = ['total_rating', 'popularity_value', 'image_path', 'name', 'address', 'score']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for shop in top_shops:
            score = shop.total_rating * Decimal('0.6') + shop.popularity_value * Decimal('0.4')
            writer.writerow({
                'total_rating': shop.total_rating,
                'popularity_value': shop.popularity_value,
                'image_path': shop.image_path,
                'name': shop.name,
                'address': shop.address,
                'score': round(score, 1)
            })

    # Read, sort by score, and select top 8
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        sorted_list = sorted(reader, key=lambda row: float(row['score']), reverse=True)[:8]

    # Recreate the CSV with sorted top 8 entries
    with open(csv_file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sorted_list)

    # Return JsonResponse for the top 8 shops
    from django.http import JsonResponse
    return JsonResponse(list(sorted_list), safe=False)


# -- get the most sales store--
# 按照商店shop中所有product的销量之和 （商店的总销量）来排序
def get_sales(request):
    # 在数据库中查找的商店信息并返回到前端
    # TODO: 创建一个csv文件叫sales.csv位于dataset_base_dir = os.path.join(settings.BASE_DIR, 'Dataset')中
    # TODO: 若该csv文件已存在,则重新覆盖该文件
    # csv文件中的数据如下:1.total_rating(float) 2.popularity_value（int） 3.image_path(string) 4.name(string) 5.address(string) 6. total_sales(float)
    # 对于popularity_value的值，是以每一个shop为单位，获取其对应ShopRating表格中对应的数据的数量。获取完毕后，再将其存入csv文件中对应的数据中
    # TODO: 对于Shop表格中的每个商店，通过shop查找其在Merchant表格中的数据，再通过merchant来查找其在Order表格中所有对应的orderd,然后再通过order在OrderItem中寻找所有对应的数据中的quantity的数据，然后进行求和，这个数据叫total_sales
    # TODO:然后根据这个数据从高到低排序,取前10名的所有csv需要的数据存入csv文件中
    # TODO:返回csv中前3个商店的信息
    dataset_base_dir = os.path.join(settings.BASE_DIR, 'Dataset')
    csv_file_path = os.path.join(dataset_base_dir, 'sales.csv')
    print(f"sales.cv path: {csv_file_path}") # 可删除

    # get the store total_sales
    shops_with_sales = Shop.objects.annotate(
        total_sales=Sum('products__order_items__quantity')
    ).order_by('-total_sales')[:10]

    # 创建或覆盖CSV文件
    with open(csv_file_path, 'w', newline='') as csvfile:
        fieldnames = ['total_rating', 'popularity_value', 'image_path', 'name', 'address', 'total_sales']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for shop in shops_with_sales:
            popularity_value = ShopRating.objects.filter(shop=shop).count()
            writer.writerow({
                'total_rating': shop.total_rating,
                'popularity_value': popularity_value,
                'image_path': shop.image_path,
                'name': shop.name,
                'address': shop.address,
                'total_sales': getattr(shop, 'total_sales', 0)  # 使用getattr以防total_sales为None
            })

    # 读取CSV文件返回前3个商店的信息
    top_3_shops = []
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in list(reader)[:3]:
            top_3_shops.append(row)

    return JsonResponse(top_3_shops, safe=False)
