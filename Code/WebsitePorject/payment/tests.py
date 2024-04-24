import json
from decimal import Decimal

import pytest
from django.urls import reverse
from django.test import RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from orders.models import Order, OrderItem
from accounts.models import Customer, Address, Shop, Merchant
from merchants.models import Product
from payment.views import generate_payment

@pytest.fixture
def rf():
    return RequestFactory()

# Helper function to add session middleware to requests
# def add_session_to_request(request, session_dict):
#     middleware = SessionMiddleware()
#     middleware.process_request(request)
#     request.session.update(session_dict)
#     request.session.save()

def add_session_to_request(request):
    middleware = SessionMiddleware(lambda x: x)
    middleware.process_request(request)
    request.session.save()


@pytest.fixture
def customer(db):
    return Customer.objects.create(username='TestUser1', password='password123', phone_number='12345678901')


@pytest.fixture
def address(customer, db):
    return Address.objects.create(
        customer=customer,
        address_line='123 Test St',
        province='TestProvince',
        city='TestCity',
        district='TestDistrict',
        detail='Test Detail'
    )


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
def merchant(db):
    return Merchant.objects.create(username='merchantuser', password='merchantpass', phone_number='9876543210')


@pytest.fixture
def product(shop, db):
    return Product.objects.create(
        name="Test Product1",
        price=Decimal("21.0"),
        description="Test Description",
        category="TestCategory",
        shop=shop,
        image_path="/path/to/image"
    )


@pytest.mark.django_db
def test_generate_payment_and_order(rf, customer, address, shop, product, merchant):
    # Setup request and session
    request = rf.post(reverse('generate_payment'), content_type='application/json')
    add_session_to_request(request)
    request.session['username'] = customer.username
    # Data to send in request
    data = {
        'products': [
            {'productId': product.id, 'quantity': 2}
        ],
        'total_price': 42.0,
        'address_id': address.id
    }
    request._body = json.dumps(data)
    response = generate_payment(request)

    # Check response
    assert response.status_code == 200
    assert json.loads(response.content)['redirect_url'] == '/payment/payment_view/'
    assert Order.objects.count() == 1
    assert OrderItem.objects.count() == 1

    # Checking the database for the created order and order item
    order = Order.objects.first()
    order_item = OrderItem.objects.first()
    assert order.customer == customer
    assert order.total_price == 42.00
    assert order_item.product == product
    assert order_item.quantity == 2
