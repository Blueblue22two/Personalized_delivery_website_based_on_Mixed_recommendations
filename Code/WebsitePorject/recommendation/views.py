from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count, Sum, Avg
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import logout
from decimal import Decimal
from django.conf import settings
from django.shortcuts import render
import logging
import csv
import os
# model
from accounts.models import Customer, Shop, Favorite
from merchants.models import Product, ShopRating
from orders.models import Order, OrderItem
from customers.models import Comment, FavItem
# math
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import jaccard_score
import numpy as np
import pandas as pd
from decimal import Decimal

logger = logging.getLogger(__name__)
# Create your views here.


# -- logout(clear session) & redirect to main page--
def logout_view(request):
    print("log out...")
    logout(request)
    print("log out successfully,redirect to /")
    return HttpResponseRedirect('/')


# item-based popularity recommendation
# recommend product based on the popularity and sales of product
def cold_start_recommendation():
    dataset_base_dir = os.path.join(settings.BASE_DIR, 'Dataset')
    if not os.path.exists(dataset_base_dir):
        os.makedirs(dataset_base_dir)
    filepath = os.path.join(dataset_base_dir, 'cold_start.csv')
    try:
        products = Product.objects.annotate(
            favorite_count=Count('favored_by'),
            total_sales=Sum('order_items__quantity')
        ).values('id', 'average_rate', 'favorite_count', 'total_sales')
        df = pd.DataFrame(list(products))

        # Convert decimal.Decimal to float
        df['average_rate'] = df['average_rate'].astype(float)
        df['favorite_count'] = df['favorite_count'].astype(float)
        df['total_sales'] = df['total_sales'].astype(float)

        # Normalize data
        df['norm_average_rate'] = df['average_rate'] / 5.0
        df['norm_favorite_count'] = df['favorite_count'] / 1000.0
        df['norm_total_sales'] = df['total_sales'] / 5000.0

        # Ensure no division by zero issues, replace NaN with 0
        df[['norm_favorite_count', 'norm_total_sales']] = df[['norm_favorite_count', 'norm_total_sales']].fillna(0)

        # Calculate recommendation score
        df['recommend_score'] = (df['norm_average_rate'] * 0.4 +
                                 df['norm_favorite_count'] * 0.3 +
                                 df['norm_total_sales'] * 0.3)
        df.to_csv(filepath, index=False)
        print(f"cold start data saved to {filepath}")
        logger.info(f"cold start data saved to {filepath}")
    except Exception as e:
        logger.error(f"Error during generating content based recommendation: {e}", exc_info=True)


# Content-based recommendation
def content_based_recommendation(user_id):
    dataset_base_dir = os.path.join(settings.BASE_DIR, 'Dataset')
    csv_file_path = os.path.join(dataset_base_dir, 'cb.csv')
    if not os.path.exists(csv_file_path):
        os.makedirs(csv_file_path)

    user = Customer.objects.get(id=user_id)
    orders = Order.objects.filter(customer=user)
    favorites = FavItem.objects.filter(customer=user)
    comments = Comment.objects.filter(customer=user, rating__gte=4.0)

    # get all products
    all_products = Product.objects.all()

    # Create feature matrix for all products
    categories = np.array([product.category for product in all_products])
    one_hot_encoder = OneHotEncoder()
    category_features = one_hot_encoder.fit_transform(categories.reshape(-1, 1)).toarray()

    numeric_features = np.array([
        [int(product.average_rate > 0),
         int(product.favored_by.count() > 0),
         int(product.order_items.aggregate(total_sales=Count('id'))['total_sales'] > 0),
         int(product.comments.count() > 0)]
        for product in all_products
    ])

    # Combine category and numeric features
    feature_matrix = np.hstack((category_features, numeric_features))

    # Map product IDs to their indices in the feature matrix
    product_index_map = {product.id: idx for idx, product in enumerate(all_products)}

    # Fetch products user has interacted with
    bought_products_ids = OrderItem.objects.filter(order__in=orders).values_list('product_id', flat=True)
    favored_product_ids = [fav.product_id for fav in favorites]
    rated_products_ids = [comment.product_id for comment in comments if comment.rating >= 3.5]

    # Build user profile based on interactions
    user_profile = np.zeros(feature_matrix.shape[1])
    for pid in set(bought_products_ids):
        user_profile += feature_matrix[product_index_map[pid], :]
    for pid in set(favored_product_ids):
        user_profile += feature_matrix[product_index_map[pid], :]
    for pid in set(rated_products_ids):
        user_profile += feature_matrix[product_index_map[pid], :]

    # Normalize user profile to binary
    user_profile = np.array(user_profile > 0, dtype=int)

    # Compute Jaccard similarity between user profile and all products
    similarities = np.array([jaccard_score(user_profile, f, average='binary') for f in feature_matrix])

    # Save similarities to CSV
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Product ID', 'Similarity'])
        for index, similarity in enumerate(similarities):
            writer.writerow([all_products[index].id, similarity])

    # Get top 20 similar products
    similar_indices = np.argsort(similarities)[::-1][:20]
    print(f"number of cb product list: {len(similar_indices)}")
    recommended_product_ids = [all_products[int(i)].id for i in similar_indices]  # Convert to int
    return recommended_product_ids


# adjust cosine similarity
def adjusted_cosine_similarity(user_item_matrix):
    # Calculate the average rating for each user
    user_ratings_mean = np.mean(user_item_matrix, axis=1)
    # 中心化处理：将用户评分减去该用户的平均评分
    matrix_user_mean = user_item_matrix.sub(user_ratings_mean, axis=0)
    # 计算修正的余弦相似度
    similarity_matrix = np.dot(matrix_user_mean, matrix_user_mean.T) / \
                        (np.linalg.norm(matrix_user_mean, axis=1)[:, np.newaxis] * \
                         np.linalg.norm(matrix_user_mean.T, axis=0)[np.newaxis, :])
    # 将NaN值填充为0（因为中心化可能导致除以0的情况）
    similarity_matrix = np.nan_to_num(similarity_matrix)
    return similarity_matrix


# User based Collaborative filtering function
def user_cf_recommendation():
    print("user_cf_recommendation function working...")
    dataset_base_dir = os.path.join(settings.BASE_DIR, 'Dataset')
    if not os.path.exists(dataset_base_dir):
        os.makedirs(dataset_base_dir)

    try:
        # create Item-User table
        favorites = FavItem.objects.values_list('product_id', 'customer_id')
        order_items = OrderItem.objects.annotate(count=Count('id')).filter(count__gt=3).values_list('product_id',
                                                                                                    'order__customer_id')
        high_ratings = Comment.objects.values('product_id').annotate(avg_rating=Avg('rating')).filter(
            avg_rating__gt=4.0).values_list('product_id', 'customer_id')

        all_likes = list(favorites) + list(order_items) + list(high_ratings)
        likes_df = pd.DataFrame(all_likes, columns=['product_id', 'user_id'])
        likes_df.drop_duplicates(inplace=True)  # remove duplicate item

        # save Item_User.csv file
        item_user_filepath = os.path.join(dataset_base_dir, 'Item_User.csv')
        likes_df.to_csv(item_user_filepath, index=False)

        user_item_matrix = pd.crosstab(likes_df.user_id, likes_df.product_id)
        # Use adjusted_cosine_similarity to calculate user similarity
        similarity_matrix = adjusted_cosine_similarity(user_item_matrix)
        np.fill_diagonal(similarity_matrix, 0)

        # save user_similarity_matrix.csv file
        user_similarity_filepath = os.path.join(dataset_base_dir, 'user_similarity_matrix.csv')
        print(f"User-similarity matrix saved to {user_similarity_filepath}")
        pd.DataFrame(similarity_matrix, index=user_item_matrix.index, columns=user_item_matrix.index).to_csv(
            user_similarity_filepath)
    except Exception as e:
        print(f"Error during generating user cf recommendation: {e}")


def weighted_hybrid_recommendation(cb_products, user_cf_products, cb_weight, user_cf_weight):
    cb_weight = Decimal(str(cb_weight))
    user_cf_weight = Decimal(str(user_cf_weight))
    combined_scores = {}
    cb_dict = {product['id']: product for product in cb_products}
    user_cf_dict = {product['id']: product for product in user_cf_products}

    # calculate the cb weight score
    for product_id, product in cb_dict.items():
        average_rate = Decimal(product.get('average_rate', 0))
        combined_scores[product_id] = combined_scores.get(product_id, Decimal('0')) + cb_weight * average_rate

    # calculate the User-cf weight score
    for product_id, product in user_cf_dict.items():
        average_rate = Decimal(product.get('average_rate', 0))
        combined_scores[product_id] = combined_scores.get(product_id, Decimal('0')) + user_cf_weight * average_rate

    top_product_ids = sorted(combined_scores, key=lambda x: combined_scores[x], reverse=True)[:20]
    final_recommendations = [cb_dict.get(pid, None) or user_cf_dict.get(pid, None) for pid in top_product_ids]
    return final_recommendations


# filter the low rated product in recommend product list
def filter_low_rated_products(customer_id, products):
    rated_products = Comment.objects.filter(customer_id=customer_id).values('product_id').annotate(avg_rating=Avg('rating'))
    low_rated_product_ids = {prod['product_id'] for prod in rated_products if prod['avg_rating'] < 3.5}
    print(f"filter_low_rated_products numbers: {len(low_rated_product_ids)}")
    return [product for product in products if product['id'] not in low_rated_product_ids]


# get and return recommended product(dish) list
def get_recommend_dish(request):
    username = request.session.get('username', None)
    user_type = request.session.get('user_type', None)
    dataset_base_dir = os.path.join(settings.BASE_DIR, 'Dataset')
    recommend_products = []  # recommended product list

    if username is None or user_type != '1':
        # use cold_start_recommendation
        filepath = os.path.join(dataset_base_dir, 'cold_start.csv')
        cold_start_recommendation()

        if not os.path.exists(filepath) or os.stat(filepath).st_size == 0:
            logger.error(f"CSV file at {filepath} is missing or empty.")
            print(f"CSV file at {filepath} is missing or empty.")
            return JsonResponse({'error': 'Data is missing or empty'}, status=500)
        else:
            df = pd.read_csv(filepath)
            top_products_dict = df.sort_values(by='recommend_score', ascending=False).head(8).to_dict('records')
            top_product_ids = [product_dict['id'] for product_dict in top_products_dict]
            top_products = list(Product.objects.filter(id__in=top_product_ids).annotate(
                product_rate_number=Count('comments')
            ).values(
                'id', 'name', 'price', 'category', 'image_path', 'average_rate', 'product_rate_number'
            ))
    else:
        # Hybrid recommendation: user_cf_recommendation & content based recommendation
        try:
            customer = Customer.objects.get(username=username)
            customer_id = customer.id
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Customer not found'}, status=404)
        order_count = Order.objects.filter(customer=customer).count()

        # get recommend product from cb
        cb_list = content_based_recommendation(customer_id)
        cb_products = list(Product.objects.filter(id__in=cb_list).annotate(
            product_rate_number=Count('comments')
        ).values(
            'id', 'name', 'price', 'category', 'image_path', 'average_rate', 'product_rate_number'
        ))

        if order_count <= 5:
            # use cold_start_recommendation
            filepath = os.path.join(dataset_base_dir, 'cold_start.csv')
            cold_start_recommendation()

            if not os.path.exists(filepath) or os.stat(filepath).st_size == 0:
                logger.error(f"CSV file at {filepath} is missing or empty.")
                print(f"CSV file at {filepath} is missing or empty.")
                return JsonResponse({'error': 'Data is missing or empty'}, status=500)
            else:
                df = pd.read_csv(filepath)
                top_products_dict = df.sort_values(by='recommend_score', ascending=False).head(8).to_dict('records')
                top_product_ids = [product_dict['id'] for product_dict in top_products_dict]
                top_products = list(Product.objects.filter(id__in=top_product_ids).annotate(
                    product_rate_number=Count('comments')
                ).values(
                    'id', 'name', 'price', 'category', 'image_path', 'average_rate', 'product_rate_number'
                ))
        else:
            # Hybrid recommend
            # get User CF
            user_cf_recommendation()
            user_similarity_filepath = os.path.join(dataset_base_dir, 'user_similarity_matrix.csv')
            similarity_matrix = pd.read_csv(user_similarity_filepath, index_col=0)

            # get all the similar users
            similar_users = similarity_matrix[str(customer_id)].sort_values(ascending=False).head(8).index
            item_user_filepath = os.path.join(dataset_base_dir, 'Item_User.csv')
            item_user_df = pd.read_csv(item_user_filepath)

            # Get items that similar users like
            liked_items = item_user_df[item_user_df['user_id'].isin(similar_users)]
            user_cf_products_ids = liked_items['product_id'].value_counts().head(8).index
            user_cf_products = Product.objects.filter(id__in=user_cf_products_ids).values('id', 'name', 'price',
                                                                                          'category',
                                                                                          'image_path', 'average_rate')

            # hybrid weight recommend
            top_products = weighted_hybrid_recommendation(cb_products, user_cf_products, cb_weight=0.5,
                                                          user_cf_weight=0.5)
            # filter out the low rated product
            top_products = filter_low_rated_products(customer_id, top_products)

    recommend_products = list(top_products)[:8]
    for product in recommend_products:
        product_id = product['id']
        product_rate_number = Comment.objects.filter(product_id=product_id).count()
        product['product_rate_number'] = product_rate_number

    # print(recommend_products)
    print("recommend dish successfully!")
    return JsonResponse({'products': recommend_products})


# -- get the most popular store--
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
            # Fetch shop favorite count
            shop_fav_number = Favorite.objects.filter(shop=shop).count()
            # Calculate score
            score = shop.total_rating * Decimal('0.5') + shop.popularity_value * Decimal(
                '0.3') + shop_fav_number * Decimal('0.2')

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
def get_sales(request):
    dataset_base_dir = os.path.join(settings.BASE_DIR, 'Dataset')
    if not os.path.exists(dataset_base_dir):
        os.makedirs(dataset_base_dir)
    csv_file_path = os.path.join(dataset_base_dir, 'sales.csv')

    # get total sales
    shops_with_sales = Shop.objects.annotate(
        total_sales=Sum('products__order_items__quantity')
    ).order_by('-total_sales')[:24]

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
                'total_sales': getattr(shop, 'total_sales', 0)
            })

    top_3_shops = []
    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in list(reader)[:3]:
            top_3_shops.append(row)

    return JsonResponse(top_3_shops, safe=False)


# search function
def get_search(request):
    if request.method == 'POST':
        s = request.POST.get('s', '')  # get the search text
        # search shop
        shop_results = Shop.objects.filter(name__icontains=s).annotate(
            shop_rate_number=Count('ratings')
        ).order_by('-total_rating').values(
            'id', 'name', 'total_rating', 'image_path', 'address', 'shop_rate_number'
        )
        # search product
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
        # default
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


# return all favorite info of the customer
def get_favorite(request):
    username = request.session.get('username', None)
    user_type = request.session.get('user_type', None)
    if username and user_type == '1':
        try:
            customer = Customer.objects.get(username=username)
            # shop info
            shop_results = Favorite.objects.filter(user=customer).annotate(
                shop_rate_number=Count('shop__favorited_by')  # Counts the number of favorites for each shop
            ).order_by('-shop__total_rating').values(
                'shop__id', 'shop__name', 'shop__total_rating', 'shop__image_path', 'shop__address', 'shop_rate_number'
            )
            # product info
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


# get the info of all the recommended product, and redirect to the page
def all_recommend(request):
    if request.method == 'POST':
        username = request.session.get('username', None)
        user_type = request.session.get('user_type', None)

        dataset_base_dir = os.path.join(settings.BASE_DIR, 'Dataset')
        cold_start_filepath = os.path.join(dataset_base_dir, 'cold_start.csv')
        item_user_filepath = os.path.join(dataset_base_dir, 'Item_User.csv')
        user_similarity_filepath = os.path.join(dataset_base_dir, 'user_similarity_matrix.csv')
        products = []  # recommended product list

        if username and user_type == '1':
            try:
                customer = Customer.objects.get(username=username)
                customer_id = customer.id
            except ObjectDoesNotExist:
                return JsonResponse({'error': 'Customer not found'}, status=404)
            customer_orders_count = Order.objects.filter(customer__username=username).count()
            if customer_orders_count > 5:
                # Hybrid
                similarity_matrix = pd.read_csv(user_similarity_filepath, index_col=0)

                # Get user CF products
                similar_users = similarity_matrix[str(customer_id)].sort_values(ascending=False).head(20).index
                item_user_df = pd.read_csv(item_user_filepath)
                liked_product_ids = item_user_df[item_user_df['user_id'].isin(similar_users)][
                    'product_id'].value_counts().head(20).index
                user_cf_products = list(
                    Product.objects.filter(id__in=liked_product_ids).values('id', 'name', 'price', 'category',
                                                                            'image_path', 'average_rate'))

                # Get cb products
                cb_product_ids = content_based_recommendation(customer_id)
                cb_products = list(
                    Product.objects.filter(id__in=cb_product_ids).values('id', 'name', 'price', 'category',
                                                                         'image_path', 'average_rate'))
                # Weighted hybrid recommendation
                top_products = weighted_hybrid_recommendation(cb_products, user_cf_products, cb_weight=0.5,
                                                              user_cf_weight=0.5)

                top_products = [p['id'] for p in top_products]
                print("all_recommend(): hybrid recommend successfully")
            else:
                # use cold_start_recommendation
                filepath = os.path.join(dataset_base_dir, 'cold_start.csv')
                cold_start_recommendation()

                if not os.path.exists(filepath) or os.stat(filepath).st_size == 0:
                    logger.error(f"CSV file at {filepath} is missing or empty.")
                    print(f"CSV file at {filepath} is missing or empty.")
                    return JsonResponse({'error': 'Data is missing or empty'}, status=500)
                else:
                    df = pd.read_csv(filepath)
                    top_products_dict = df.sort_values(by='recommend_score', ascending=False).head(20).to_dict('records')
                    top_products = [product_dict['id'] for product_dict in top_products_dict]

            products_queryset = Product.objects.filter(id__in=top_products)
            products = list(products_queryset.annotate(product_rate_number=Count('comments')).values(
                'id', 'name', 'price', 'category', 'image_path', 'average_rate', 'product_rate_number'))
            if username:
                products = filter_low_rated_products(customer_id, products)  # filer out low rated
        else:
            # cold start recommendation
            df = pd.read_csv(cold_start_filepath)
            product_ids = df.sort_values(by='recommend_score', ascending=False).head(20)['id']
            products_queryset = Product.objects.filter(id__in=product_ids)
            print("all_recommend(): cold start recommend successfully")
            products = list(products_queryset.annotate(product_rate_number=Count('comments')).values(
                'id', 'name', 'price', 'category', 'image_path', 'average_rate', 'product_rate_number'))
        return JsonResponse({'products': products, 'type': 'product'})
    else:
        context = {'type': 'recommend'}
        return render(request, 'view.html', context)


# get the info of all the most popular store, and redirect to the page
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


# get the info of all the most sales store, and redirect to the page
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
