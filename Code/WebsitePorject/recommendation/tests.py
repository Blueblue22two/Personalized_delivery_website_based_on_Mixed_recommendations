import os
import pandas as pd
import pytest
from django.db.models import Count, Avg
from WebsitePorject import settings
from recommendation.views import content_based_recommendation, user_cf_recommendation, weighted_hybrid_recommendation
from merchants.models import Product
from customers.models import Customer, FavItem, Comment
from orders.models import OrderItem
import logging

logger = logging.getLogger(__name__)


def calculate_metrics(recommended_products, actual_likes):
    true_positives = len(set(recommended_products) & set(actual_likes))
    precision = true_positives / len(recommended_products) if recommended_products else 0
    recall = true_positives / len(actual_likes) if actual_likes else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) else 0
    return precision, recall, f1


def get_actual_likes(customer):
    favorited_products = FavItem.objects.filter(customer=customer).values_list('product_id', flat=True)
    frequently_bought_products = OrderItem.objects.filter(customer=customer) \
        .values('product_id') \
        .annotate(total_count=Count('id')) \
        .filter(total_count__gt=2) \
        .values_list('product_id', flat=True)
    highly_rated_products = Comment.objects.filter(customer=customer) \
        .values('product_id') \
        .annotate(avg_rating=Avg('rating')) \
        .filter(avg_rating__gt=3.5) \
        .values_list('product_id', flat=True)

    actual_likes = set(list(favorited_products) + list(frequently_bought_products) + list(highly_rated_products))
    return list(actual_likes)


# filter the low rated product in recommend product list
def filter_low_rated_products(customer_id, products):
    rated_products = Comment.objects.filter(customer_id=customer_id).values('product_id').annotate(avg_rating=Avg('rating'))
    low_rated_product_ids = {prod['product_id'] for prod in rated_products if prod['avg_rating'] < 3.5}
    print(f"filter_low_rated_products numbers: {len(low_rated_product_ids)}")
    return [product for product in products if product['id'] not in low_rated_product_ids]


def get_user_cf_products(item_user_filepath, user_similarity_filepath,customer_id):
    user_cf_recommendation()
    similarity_matrix = pd.read_csv(user_similarity_filepath, index_col=0)
    # Get user CF products
    similar_users = similarity_matrix[str(customer_id)].sort_values(ascending=False).head(20).index
    item_user_df = pd.read_csv(item_user_filepath)
    liked_product_ids = item_user_df[item_user_df['user_id'].isin(similar_users)][
        'product_id'].value_counts().head(20).index
    user_cf_products = list(
        Product.objects.filter(id__in=liked_product_ids).values('id', 'name', 'price', 'category',
                                                                'image_path', 'average_rate'))
    # user_cf_products = filter_low_rated_products(customer_id,user_cf_products)
    return user_cf_products


def get_cb(customer_id):
    logger.info("Generating content-based recommendations")
    try:
        cb_product_ids = content_based_recommendation(customer_id)
        if not cb_product_ids:
            print("cb_product_ids none")
            logger.warning("No CB products found.")
        cb_products = list(Product.objects.filter(id__in=cb_product_ids).values(
            'id', 'name', 'price', 'category', 'image_path', 'average_rate'))
        if not cb_products:
            logger.warning("No CB products found.")
        return cb_products
    except Exception as e:
        logger.error(f"Error during CB recommendation: {e}")
        return []


def get_cold_start_products(filepath, customer_id):
    logger.info("Starting cold start recommendation")
    try:
        df = pd.read_csv(filepath)
        if df.empty:
            logger.warning("Cold start CSV is empty.")
        product_ids = df.sort_values(by='recommend_score', ascending=False).head(20)['id']
        products_queryset = Product.objects.filter(id__in=product_ids)
        products = list(products_queryset.annotate(product_rate_number=Count('comments')).values(
            'id', 'name', 'price', 'category', 'image_path', 'average_rate', 'product_rate_number'))
        logger.info(f"Number of cold start products: {len(products)}")
        return products
    except Exception as e:
        logger.error(f"Error in cold start recommendation: {e}")
        return []


@pytest.mark.django_db
def test_recommendation_system():
    dataset_base_dir = os.path.join(settings.BASE_DIR, 'Dataset')
    print(f"datset path:{dataset_base_dir}")
    cold_start_filepath = os.path.join(dataset_base_dir, 'cold_start.csv')
    print(f"cold_start path:{cold_start_filepath}")
    item_user_filepath = os.path.join(dataset_base_dir, 'Item_User.csv')
    user_similarity_filepath = os.path.join(dataset_base_dir, 'user_similarity_matrix.csv')
    print(f"user_similarity_filepath path:{user_similarity_filepath}")

    customers = Customer.objects.all()[:5]  # 获取前5个客户
    metrics = {'cold_start': [], 'cb': [], 'user_cf': [], 'hybrid': []}

    print("customers:")
    print(customers)
    for customer in customers:
        actual_likes = get_actual_likes(customer)

        cold_start_products = get_cold_start_products(cold_start_filepath, customer.id)
        if not cold_start_products:
            print(f"Warning: No cold start products for customer {customer.id}")

        cb_products = get_cb(customer.id)
        if not cb_products:
            print(f"Warning: No content-based products for customer {customer.id}")

        user_cf_products = get_user_cf_products(item_user_filepath, user_similarity_filepath, customer.id)
        if not user_cf_products:
            print(f"Warning: No user CF products for customer {customer.id}")

        hybrid_products = weighted_hybrid_recommendation(cb_products, user_cf_products, 0.5, 0.5)
        if not hybrid_products:
            print(f"Warning: No hybrid products for customer {customer.id}")

        metrics['cold_start'].append(calculate_metrics(cold_start_products, actual_likes))
        metrics['cb'].append(calculate_metrics(cb_products, actual_likes))
        metrics['user_cf'].append(calculate_metrics(user_cf_products, actual_likes))
        metrics['hybrid'].append(calculate_metrics(hybrid_products, actual_likes))

    # average
    for method, values in metrics.items():
        if values:
            avg_precision = sum(x[0] for x in values) / len(values)
            avg_recall = sum(x[1] for x in values) / len(values)
            avg_f1 = sum(x[2] for x in values) / len(values)
            print(
                f"{method.capitalize()} - Average Precision: {avg_precision:.3f}, Average Recall: {avg_recall:.3f}, Average F1: {avg_f1:.3f}")
        else:
            print(f"{method.capitalize()} - No data available to calculate metrics.")

