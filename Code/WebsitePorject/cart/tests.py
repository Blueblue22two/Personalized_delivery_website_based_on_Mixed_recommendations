import json
import pytest
from django.urls import reverse
from django.test import RequestFactory
from accounts.models import Customer, ShoppingCart, Shop, Merchant
from cart.models import CartItem
from cart.views import add_cart
from merchants.models import Product
from django.contrib.sessions.middleware import SessionMiddleware


# Helper to add session middleware to requests
def add_session_to_request(request):
    middleware = SessionMiddleware(lambda x: x)
    middleware.process_request(request)
    request.session.save()


@pytest.fixture
def customer():
    return Customer.objects.create(username='testuser', password='password1234', phone_number='12345678901')


@pytest.fixture
def merchant():
    return Merchant.objects.create(username='testmerchant', password='password1234', phone_number='12345678901')


@pytest.fixture
def shop(merchant):
    return Shop.objects.create(name='Test Shop', total_rating=4.0, image_path='/path/to/image', address='123 Test St', province='TestProvince', city='TestCity', district='TestDistrict', detail='TestDetail',merchant=merchant)


@pytest.fixture
def product(shop):
    return Product.objects.create(name='Test Product1', price=29.99, category='Burger', shop=shop)


@pytest.mark.django_db
def test_add_cart(customer, product, rf: RequestFactory):
    request = rf.post(reverse('add_cart'), {'productId': product.id})
    add_session_to_request(request)
    request.session['username'] = customer.username
    request.session['user_type'] = '1'
    request.user = customer
    response = add_cart(request)

    assert response.status_code == 200
    assert CartItem.objects.filter(cart__customer=customer, product=product).exists()
    assert json.loads(response.content)['message'] == f'Product {product.id} added to cart successfully.'


@pytest.mark.django_db
def test_modify_cart_item(customer, product, rf: RequestFactory):
    # Add a product to the customer's cart
    request_add = rf.post(reverse('add_cart'), {'productId': product.id})
    add_session_to_request(request_add)
    request_add.session['username'] = customer.username
    request_add.session['user_type'] = '1'
    request_add.user = customer
    add_cart(request_add)

    # Assume the cart item now exists, modify the quantity
    cart_item = CartItem.objects.get(cart__customer=customer, product=product)
    cart_item.quantity += 1  # Increase quantity by 1
    cart_item.save()

    # Fetch the updated cart item
    updated_cart_item = CartItem.objects.get(cart__customer=customer, product=product)
    assert updated_cart_item.quantity == 2
