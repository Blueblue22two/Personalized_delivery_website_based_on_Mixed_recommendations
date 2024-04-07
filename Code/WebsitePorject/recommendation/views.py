from django.db.models import Count, Sum, Avg
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth import logout
from decimal import Decimal
from django.conf import settings
from django.shortcuts import render
import csv
import os
# model
from accounts.models import Customer, Merchant, Shop, Favorite
from merchants.models import Product, ShopRating
from orders.models import Order, OrderItem
from customers.models import Comment, FavItem
# math
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
import logging

logger = logging.getLogger(__name__)


# Create your views here.


# -- logout(clear session) & redirect to main page--
def logout_view(request):
    print("log out...")
    logout(request)
    print("log out successfully,redirect to /")
    return HttpResponseRedirect('/')


# 基于内容的推荐函数，用于冷启动
def content_based_recommendation():
    """
    对于基于内容的推荐函数，基于商品的下面几种属性来生成：
    商品平均评分，商品被收藏次数，商品销量
    其中三个属性的推荐权重为2：1：1
    """
    logger.info("Starting content_based_recommendation")
    dataset_base_dir = os.path.join(settings.BASE_DIR, 'Dataset')

    if not os.path.exists(dataset_base_dir):
        os.makedirs(dataset_base_dir)
    filepath = os.path.join(dataset_base_dir, 'content_product.csv')
    try:
        products = Product.objects.annotate(
            favorite_count=Count('favored_by'),
            total_sales=Sum('order_items__quantity')
        ).values('id', 'average_rate', 'favorite_count', 'total_sales')

        # 转换为DataFrame
        df = pd.DataFrame(list(products))
        # 计算推荐得分
        df['recommend_score'] = df['average_rate'].apply(Decimal) * Decimal('2') + \
                                df['favorite_count'].apply(Decimal) * Decimal('1') + \
                                df['total_sales'].apply(Decimal) * Decimal('1')

        # 无论原本csv中之前是否存在数据，将新数据覆盖并保存到CSV文件中
        df.to_csv(filepath, index=False)
        print(f"Content-based recommendation data saved to {filepath}")
        logger.info(f"Content-based recommendation data saved to {filepath}")
    except Exception as e:
        logger.error(f"Error during generating content based recommendation: {e}", exc_info=True)
        print(f"Error during generating content based recommendation: {e}")


# 基于用户的协同过滤推荐函数，生成用户特征矩阵
def user_cf_recommendation():
    print("user_cf_recommendation function working...")
    dataset_base_dir = os.path.join(settings.BASE_DIR, 'Dataset')
    if not os.path.exists(dataset_base_dir):
        os.makedirs(dataset_base_dir)

    try:
        # 创建Item-User表,倒排表
        favorites = FavItem.objects.values_list('product_id', 'customer_id')
        order_items = OrderItem.objects.annotate(count=Count('id')).filter(count__gt=3).values_list('product_id',
                                                                                                    'order__customer_id')
        high_ratings = Comment.objects.values('product_id').annotate(avg_rating=Avg('rating')).filter(
            avg_rating__gt=4.0).values_list('product_id', 'customer_id')

        # 合并这些查询集
        all_likes = list(favorites) + list(order_items) + list(high_ratings)

        # 转换成DataFrame
        likes_df = pd.DataFrame(all_likes, columns=['product_id', 'user_id'])
        likes_df.drop_duplicates(inplace=True)  # 移除重复项

        # 保存Item-User表到CSV
        item_user_filepath = os.path.join(dataset_base_dir, 'Item_User.csv')
        likes_df.to_csv(item_user_filepath, index=False)

        # 建立用户喜爱物品交集矩阵
        user_item_matrix = pd.crosstab(likes_df.user_id, likes_df.product_id)

        # 计算用户相似度矩阵
        similarity_matrix = cosine_similarity(user_item_matrix)
        np.fill_diagonal(similarity_matrix, 0)  # 将对角线设置为0，用户与自己的相似度不考虑

        # 保存用户相似度矩阵到CSV
        # 无论原本csv中之前是否存在数据，将新数据覆盖并保存到CSV文件中
        user_similarity_filepath = os.path.join(dataset_base_dir, 'user_similarity_matrix.csv')
        pd.DataFrame(similarity_matrix, index=user_item_matrix.index, columns=user_item_matrix.index).to_csv(
            user_similarity_filepath)
    except Exception as e:
        print(f"Error during generating user cf recommendation: {e}")


# 推荐函数，对于用户的登录状态与登录类型来为推荐商品给用户
# 当用户为登录状态且用户类型为customer时则使用user_cf_recommendation()
# 其他情况都使用content_based_recommendation()
def get_recommend_dish(request):
    username = request.session.get('username', None)
    user_type = request.session.get('user_type', None)  # '1'表示customer

    recommend_products = []  # 初始化推荐的商品列表
    dataset_base_dir = os.path.join(settings.BASE_DIR, 'Dataset')

    if username is None or user_type != '1':
        # content_based_recommendation
        content_based_recommendation()
        filepath = os.path.join(dataset_base_dir, 'content_product.csv')
        if not os.path.exists(filepath) or os.stat(filepath).st_size == 0:
            logger.error(f"CSV file at {filepath} is missing or empty.")
            print(f"CSV file at {filepath} is missing or empty.")
            return JsonResponse({'error': 'Data is missing or empty'}, status=500)
        else:
            df = pd.read_csv(filepath)
            # 转化为字典并排序
            top_products_dict = df.sort_values(by='recommend_score', ascending=False).head(8).to_dict('records')
            # 从top_products_dict中get product ID
            top_product_ids = [product_dict['id'] for product_dict in top_products_dict]

            top_products = list(Product.objects.filter(id__in=top_product_ids).annotate(
                product_rate_number=Count('comments')
            ).values(
                'id', 'name', 'price', 'category', 'image_path', 'average_rate', 'product_rate_number'
            ))
    else:
        # user_cf_recommendation
        customer = Customer.objects.get(username=username)
        customer_id = customer.id
        order_count = Order.objects.filter(customer=customer).count()
        user_cf_recommendation()

        if order_count < 3:  # 对于购买订单小于3的用户也使用 content_based_recommendation
            filepath = os.path.join(dataset_base_dir, 'content_product.csv')
            df = pd.read_csv(filepath)
            top_products_dict = df.sort_values(by='recommend_score', ascending=False).head(8).to_dict('records')
            top_product_ids = [product_dict['id'] for product_dict in top_products_dict]
            top_products = list(Product.objects.filter(id__in=top_product_ids).annotate(
                product_rate_number=Count('comments')
            ).values(
                'id', 'name', 'price', 'category', 'image_path', 'average_rate', 'product_rate_number'
            ))
        else:
            user_similarity_filepath = os.path.join(dataset_base_dir, 'user_similarity_matrix.csv')
            similarity_matrix = pd.read_csv(user_similarity_filepath, index_col=0)

            # 若customer_id不在相似度矩阵中，使用内容推荐
            if str(customer_id) not in similarity_matrix.columns:
                print(f"customer id: {customer_id} was not found in the user_similarity_matrix.csv")
                filepath = os.path.join(dataset_base_dir, 'content_product.csv')
                df = pd.read_csv(filepath)
                top_products_dict = df.sort_values(by='recommend_score', ascending=False).head(8).to_dict('records')
                top_product_ids = [product_dict['id'] for product_dict in top_products_dict]
                top_products = list(Product.objects.filter(id__in=top_product_ids).annotate(
                    product_rate_number=Count('comments')
                ).values(
                    'id', 'name', 'price', 'category', 'image_path', 'average_rate', 'product_rate_number'
                ))
            else:
                # 获取与用户最相似的用户列表
                similar_users = similarity_matrix[str(customer_id)].sort_values(ascending=False).head(8).index
                item_user_filepath = os.path.join(dataset_base_dir, 'Item_User.csv')
                item_user_df = pd.read_csv(item_user_filepath)

                # 获取相似用户喜欢的商品
                liked_items = item_user_df[item_user_df['user_id'].isin(similar_users)]
                top_products_ids = liked_items['product_id'].value_counts().head(8).index
                top_products = Product.objects.filter(id__in=top_products_ids).values('id', 'name', 'price', 'category',
                                                                                      'image_path', 'average_rate')

    # 将查询集转换为列表字典
    recommend_products = list(top_products)

    # 获取每个推荐产品的评价数量
    for product in recommend_products:
        product_id = product['id']
        product_rate_number = Comment.objects.filter(product_id=product_id).count()
        product['product_rate_number'] = product_rate_number
    print("recommend dish successfully")
    return JsonResponse({'products': recommend_products})


# -- get the most popular store--
#     # 在数据库中查找的商店信息并返回到前端
#     # 创建一个csv文件叫popular.csv位于dataset_base_dir = os.path.join(settings.BASE_DIR, 'Dataset')中
#     # csv文件中的数据1.total_rating(float) 2.popularity_value（int） 3.image_path(string) 4.name(string) 5.address(string) 6. score(float)
#     # 以一个shop为单位，在Shop表格中先按照total_rating的数值从高到低排序，取排名前24的shop的total_rating, image_path ,name, address先存入该csv文件中
#     # 对于popularity_value的值，是以每一个shop为单位，获取其对应ShopRating表格中对应的数据的数量。获取完毕后，再将其存入csv文件中对应的数据中
#     # 然后对csv中每条数据，取其total_rating与popularity_value按照 score = total_rating*0.6 + popularity_value*0.4的公式计算出score(score保留一位小数)
#     # 对这个csv文件按照score的数值从大到小重新排序
#     # 按照排序的顺序，仅返回csv中排名前8的所有数据

def get_popular(request):
    dataset_base_dir = os.path.join(settings.BASE_DIR, 'Dataset')
    if not os.path.exists(dataset_base_dir):
        os.makedirs(dataset_base_dir)
    # path of csv file
    csv_file_path = os.path.join(dataset_base_dir, 'popular.csv')
    # Fetch top 24 shops based on total_rating
    top_shops = Shop.objects.annotate(popularity_value=Count('ratings')).order_by('-total_rating')[:24]

    # Prepare CSV data
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['total_rating', 'popularity_value', 'image_path', 'name', 'address', 'score']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        shops_list = []
        for shop in top_shops:
            score = shop.total_rating * Decimal('0.6') + shop.popularity_value * Decimal('0.4')
            shop_dict = {
                'total_rating': shop.total_rating,
                'popularity_value': shop.popularity_value,
                'image_path': shop.image_path,
                'name': shop.name,
                'address': shop.address,
                'score': round(score, 1)
            }
            writer.writerow(shop_dict)
            shops_list.append(shop_dict)


    # Read the CSV, sort by 'score', and rewrite the sorted data back to the CSV
    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = list(csv.DictReader(csvfile))  # Convert iterator to list to sort
        sorted_list = sorted(reader, key=lambda x: Decimal(x['score']), reverse=True)

    # Rewrite the CSV with sorted data
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sorted_list)  # Write the sorted list back to the CSV

    popular_list = []
    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in list(reader)[:8]:
            popular_list.append(row)

    return JsonResponse({'shops': popular_list, 'type': 'shop'}, safe=False)


# -- get the most sales store--
# 按照商店shop中所有product的销量之和 （商店的总销量）来排序
# 创建一个csv文件叫sales.csv位于dataset_base_dir = os.path.join(settings.BASE_DIR, 'Dataset')中
# csv文件中的数据如下:1.total_rating(float) 2.popularity_value（int） 3.image_path(string) 4.name(string) 5.address(string) 6. total_sales(float)
# 对于popularity_value的值，是以每一个shop为单位，获取其对应ShopRating表格中对应的数据的数量。获取完毕后，再将其存入csv文件中对应的数据中
# 对于Shop表格中的每个商店，通过shop查找其在Merchant表格中的数据，
# 再通过merchant来查找其在Order表格中所有对应的orderd,然后再通过order在OrderItem中寻找所有对应的数据中的quantity的数据，然后进行求和，这个数据叫total_sales
# 然后根据total_sales数据从高到低排序,取前24名的需要的数据存入csv文件中
# 返回csv中前3个商店的信息
def get_sales(request):
    dataset_base_dir = os.path.join(settings.BASE_DIR, 'Dataset')
    if not os.path.exists(dataset_base_dir):
        os.makedirs(dataset_base_dir)

    csv_file_path = os.path.join(dataset_base_dir, 'sales.csv')

    # 获取店铺的总销量
    shops_with_sales = Shop.objects.annotate(
        total_sales=Sum('products__order_items__quantity')
    ).order_by('-total_sales')[:24]

    # 创建或覆盖CSV文件，指定编码为utf-8
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
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
                'total_sales': getattr(shop, 'total_sales', 0)  # 使用getattr防止total_sales为None
            })

    top_3_shops = []
    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in list(reader)[:3]:
            top_3_shops.append(row)

    return JsonResponse(top_3_shops, safe=False)


# search page function
def get_search(request):
    if request.method == 'POST':
        s = request.POST.get('s', '')  # get the search text

        shop_results = Shop.objects.filter(name__icontains=s).annotate(
            shop_rate_number=Count('ratings')
        ).order_by('-total_rating').values(
            'id', 'name', 'total_rating', 'image_path', 'address', 'shop_rate_number'
        )

        product_results = Product.objects.filter(name__icontains=s).annotate(
            product_rate_number=Count('comments')
        ).order_by('-average_rate').values(
            'id', 'name', 'price', 'category', 'image_path', 'average_rate', 'product_rate_number'
        )

        return JsonResponse({
            'shops': list(shop_results),
            'products': list(product_results)
        })
    else:

        shop_results = Shop.objects.annotate(
            shop_rate_number=Count('ratings')
        ).order_by('-total_rating').values(
            'id', 'name', 'total_rating', 'image_path', 'address', 'shop_rate_number'
        )

        product_results = Product.objects.annotate(
            product_rate_number=Count('comments')
        ).order_by('-average_rate').values(
            'id', 'name', 'price', 'category', 'image_path', 'average_rate', 'product_rate_number'
        )

        return JsonResponse({
            'shops': list(shop_results),
            'products': list(product_results)
        })


# return favorite info
def get_favorite(request):
    username = request.session.get('username', None)
    user_type = request.session.get('user_type', None)
    if username and user_type == '1':
        try:
            customer = Customer.objects.get(username=username)

            shop_results = Favorite.objects.filter(user=customer).annotate(
                shop_rate_number=Count('shop__favorited_by')  # Counts the number of favorites for each shop
            ).order_by('-shop__total_rating').values(
                'shop__id', 'shop__name', 'shop__total_rating', 'shop__image_path', 'shop__address', 'shop_rate_number'
            )


            product_results = FavItem.objects.filter(customer=customer).annotate(
                product_rate_number=Count('product__comments')  # Counts the number of comments for each product
            ).order_by('-product__average_rate').values(
                'product__id', 'product__name', 'product__price', 'product__category', 'product__image_path',
                'product__average_rate', 'product_rate_number'
            )

            return JsonResponse({
                'shops': list(shop_results),
                'products': list(product_results)
            })
        except Customer.DoesNotExist:
            return JsonResponse({'message': 'User does not exist.'}, status=404)
    else:
        return JsonResponse({'message': 'error: Non-existent user type.'}, status=400)


def all_recommend(request):
    if request.method == 'POST':
        username = request.session.get('username', None)
        user_type = request.session.get('user_type', None)

        dataset_base_dir = os.path.join(settings.BASE_DIR, 'Dataset')
        content_filepath = os.path.join(dataset_base_dir, 'content_product.csv')
        item_user_filepath = os.path.join(dataset_base_dir, 'Item_User.csv')
        user_similarity_filepath = os.path.join(dataset_base_dir, 'user_similarity_matrix.csv')
        products = [] # recommended product list

        if username and user_type == '1':
            customer_orders_count = Order.objects.filter(customer__username=username).count()
            if customer_orders_count > 3:
                similarity_matrix = pd.read_csv(user_similarity_filepath, index_col=0)
                customer_id = Customer.objects.get(username=username).id

                if str(customer_id) in similarity_matrix.columns:
                    # user cf recommendation
                    similar_users = similarity_matrix[str(customer_id)].sort_values(ascending=False).index[:20]
                    item_user_df = pd.read_csv(item_user_filepath)
                    liked_product_ids = item_user_df[item_user_df['user_id'].isin(similar_users)]['product_id'].value_counts().head(20).index
                    products_queryset = Product.objects.filter(id__in=liked_product_ids)
                else:
                    # content_based_recommendation
                    df = pd.read_csv(content_filepath)
                    product_ids = df.sort_values(by='recommend_score', ascending=False).head(20)['id']
                    products_queryset = Product.objects.filter(id__in=product_ids)
            else:
                # content_based_recommendation
                df = pd.read_csv(content_filepath)
                product_ids = df.sort_values(by='recommend_score', ascending=False).head(20)['id']
                products_queryset = Product.objects.filter(id__in=product_ids)
        else:
            # content_based_recommendation
            df = pd.read_csv(content_filepath)
            product_ids = df.sort_values(by='recommend_score', ascending=False).head(20)['id']
            products_queryset = Product.objects.filter(id__in=product_ids)

        products = list(products_queryset.annotate(product_rate_number=Count('comments')).values(
            'id', 'name', 'price', 'category', 'image_path', 'average_rate', 'product_rate_number'))

        return JsonResponse({'products': products, 'type': 'product'})
    else:
        context = {'type': 'recommend'}
        return render(request, 'view.html', context)


# all the most popular store page
def all_popular(request):
    if request.method == 'POST':
        dataset_base_dir = os.path.join(settings.BASE_DIR, 'Dataset')
        csv_file_path = os.path.join(dataset_base_dir, 'popular.csv')

        shops = []
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in list(reader)[:10]:
                row['shop_rate_number'] = row.pop('popularity_value')
                shops.append(row)

        return JsonResponse({'shops': shops, 'type': 'shop'})
    else:
        type_view = 'popular'
        context = {'type': type_view}
        return render(request, 'view.html', context)


# all the most sales store page
def all_sales(request):
    if request.method == 'POST':
        # get sales.csv
        dataset_base_dir = os.path.join(settings.BASE_DIR, 'Dataset')
        csv_file_path = os.path.join(dataset_base_dir, 'sales.csv')

        shops = []
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in list(csv_reader)[:10]:
                row['shop_rate_number'] = row.pop('popularity_value')
                shops.append(row)

        return JsonResponse({'shops': shops, 'type': 'shop'})
    else:
        type_view = 'sales'
        context = {'type': type_view}
        return render(request, 'view.html', context)
