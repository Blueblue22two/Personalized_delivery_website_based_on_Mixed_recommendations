import pytest
from django.urls import reverse
from django.test import RequestFactory
from accounts.models import Customer, Shop, Favorite, Address, Merchant
from customers.models import FavItem
from customers.views import cancel_product_fav, add_fav, cancel_shop_fav, add_fav_product, add_address
from merchants.models import Product
from django.contrib.sessions.middleware import SessionMiddleware
import json


# Helper to add session middleware to requests
def add_session_to_request(request):
    middleware = SessionMiddleware(lambda x: x)
    middleware.process_request(request)
    request.session.save()


@pytest.fixture
def rf():
    return RequestFactory()


@pytest.fixture
def customer(db):
    return Customer.objects.create(username='testuser', password='password1234', phone_number='12345678901')


@pytest.fixture
def merchant(db):
    return Merchant.objects.create(username='testmerchant', password='password1234', phone_number='12345678901')


@pytest.fixture
def shop(merchant, db):
    return Shop.objects.create(name='Test Shop', merchant=merchant, total_rating=4.0, image_path='/path/to/image', address='123 Test St', province='TestProvince', city='TestCity', district='TestDistrict', detail='TestDetail')


@pytest.fixture
def product(shop, db):
    return Product.objects.create(name='Test Product12', shop=shop, price=25.99, category='Pizza')


@pytest.mark.django_db
def test_add_address(customer, rf):
    request = rf.post(reverse('add_address'), {
        'province': 'TestProvince',
        'city': 'TestCity',
        'district': 'TestDistrict',
        'detail': '123 My Street'
    })
    add_session_to_request(request)
    request.session['username'] = customer.username
    request.session['user_type'] = '1'
    request.user = customer
    response = add_address(request)
    assert response.status_code == 302  # assuming redirection to '/carts/main/'
    assert Address.objects.filter(customer=customer).exists()


@pytest.mark.django_db
def test_add_fav_product(customer, product, rf):
    request = rf.post(reverse('add_fav_product'), {'productId': product.id})
    add_session_to_request(request)
    request.session['username'] = customer.username
    request.session['user_type'] = '1'
    request.user = customer
    response = add_fav_product(request)
    assert response.status_code == 200
    assert json.loads(response.content)['message'] == 'Product added to favorites successfully!'
    assert FavItem.objects.filter(customer=customer, product=product).exists()


@pytest.mark.django_db
def test_cancel_product_fav(customer, product, rf):
    FavItem.objects.create(customer=customer, product=product)
    request = rf.post(reverse('cancel_product_fav', kwargs={'id': product.id}))
    add_session_to_request(request)
    request.session['username'] = customer.username
    request.session['user_type'] = '1'
    request.user = customer
    response = cancel_product_fav(request,product.id)
    assert response.status_code == 200
    assert not FavItem.objects.filter(customer=customer, product=product).exists()


@pytest.mark.django_db
def test_add_fav_product_twice(customer, product, rf):
    # add the product to favorites
    request = rf.post(reverse('add_fav_product'), {'productId': product.id})
    add_session_to_request(request)
    request.session['username'] = customer.username
    request.session['user_type'] = '1'
    request.user = customer
    response = add_fav_product(request)
    assert response.status_code == 200
    assert json.loads(response.content)['message'] == 'Product added to favorites successfully!'

    # add the same product to favorites
    second_request = rf.post(reverse('add_fav_product'), {'productId': product.id})
    add_session_to_request(second_request)
    second_request.session['username'] = customer.username
    second_request.session['user_type'] = '1'
    second_request.user = customer
    second_response = add_fav_product(second_request)
    assert second_response.status_code == 200
    assert json.loads(second_response.content)['message'] == 'You have already added this product to favorites.'


@pytest.mark.django_db
def test_cancel_nonexistent_shop_fav(customer, rf):
    # Use a clearly non-existent shop name
    nonexistent_shop_name = "Definitely Not a Real Shop"
    request = rf.post(reverse('cancel_shop_fav', kwargs={'name': nonexistent_shop_name}))
    add_session_to_request(request)
    request.session['username'] = customer.username
    request.session['user_type'] = '1'
    request.user = customer
    response = cancel_shop_fav(request, nonexistent_shop_name)  # Pass the nonexistent shop name to the function
    assert response.status_code == 404
    assert json.loads(response.content)['message'] == 'Shop does not exist.'


