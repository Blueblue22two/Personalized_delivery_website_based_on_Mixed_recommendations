from decimal import Decimal
import json
import pytest
from django.urls import reverse
from django.test import RequestFactory
from WebsitePorject import settings
from accounts.models import Customer, Merchant, Shop
from customers.models import Comment
from merchants.models import Product, ShopRating
from django.contrib.sessions.middleware import SessionMiddleware


# Helper to add session middleware to requests
from orders.models import Order, OrderItem
from orders.views import post_comment


def add_session_to_request(request):
    middleware = SessionMiddleware(lambda x: x)
    middleware.process_request(request)
    request.session.save()


@pytest.fixture
def rf():
    return RequestFactory()


@pytest.fixture
def customer(db):
    return Customer.objects.create(username='TestCustomer1', password='password123456', phone_number='17345678901')


@pytest.fixture
def merchant(db):
    return Merchant.objects.create(username='TestMerchant1', password='password1234', phone_number='12345678901')


@pytest.fixture
def shop(merchant, db):
    shop = Shop.objects.create(
            merchant=merchant,
            name="TestShop1",
            total_rating=4.0,
            image_path="/path/to/image",
            address="123 Test St",
            province="TestProvince",
            city="TestCity",
            district="TestDistrict",
            detail="Detail Info"
    )
    merchant.shop = shop
    merchant.save()
    return shop


@pytest.fixture
def product(shop, db):
    return Product.objects.create(
        name="Test Product",
        price=Decimal("25.0"),
        description="Test Description",
        category="TestCategory",
        shop=shop,
        image_path="/path/to/image"
    )


@pytest.fixture
def order(customer, merchant,shop, product, db):
    order = Order.objects.create(
        customer=customer,
        merchant=merchant,
        shop=shop,
        total_price=Decimal('100.00')
    )
    OrderItem.objects.create(
        order=order,
        product=product,
        product_price=product.price,
        quantity=4
    )
    return order


def test_post_comment(rf, customer, shop, product, order):
    url = reverse('post_comment')
    data = {
        'order_id': order.id,
        'shopRating': '4.5',
        'commentText': 'Great product!',
        'productRatings': [
            {'name': product.name, 'rating': '4.5'}
        ]
    }
    request = rf.post(url, json.dumps(data), content_type='application/json')

    # Add session data to request
    add_session_to_request(request)
    request.session['username'] = customer.username
    request.session['user_type'] = '1'
    response = post_comment(request)
    assert response.status_code == 200
    assert json.loads(response.content)['success'] == True
    assert ShopRating.objects.count() == 1
    assert Comment.objects.count() == 1
    shop.refresh_from_db()
    assert shop.total_rating == Decimal('4.5')
    product.refresh_from_db()
    assert product.get_average_rate() == Decimal('4.5')

