import pytest
from django.urls import reverse
from django.test import RequestFactory
from accounts.views import login_customer, logout_view, customer_register, merchant_register
from accounts.models import Customer, Merchant
from django.contrib.sessions.middleware import SessionMiddleware
import json


# Helper to add session middleware to requests
def add_session_to_request(request):
    middleware = SessionMiddleware(lambda x: x)
    middleware.process_request(request)
    request.session.save()


# Fixture for the request factory
@pytest.fixture
def rf():
    return RequestFactory()


# test register of customer
@pytest.mark.django_db
def test_customer_registration(rf):
    url = reverse('customer_register')
    data = {'username': 'newcustomer', 'password': 'securepass123', 'phone': '12345678901', 'userType': '1'}
    request = rf.post(url, data)
    add_session_to_request(request)
    response = customer_register(request)
    assert response.status_code == 200
    assert Customer.objects.filter(username='newcustomer').exists()


# test register of customer with duplicate username
@pytest.mark.django_db
def test_customer_registration_duplicate_username(rf):
    # First registration attempt
    url = reverse('customer_register')
    data = {'username': 'duplicateuser', 'password': 'securepass123', 'phone': '12345678901', 'userType': '1'}
    request = rf.post(url, data)
    add_session_to_request(request)
    first_response = customer_register(request)
    assert first_response.status_code == 200
    assert Customer.objects.filter(username='duplicateuser').exists()

    # Second registration attempt with the same username
    request2 = rf.post(url, data)
    add_session_to_request(request2)
    response2 = customer_register(request2)
    assert response2.status_code == 409
    assert response2.json()['message'] == 'Error: Already have a same username.'


# test register for merchant
@pytest.mark.django_db
def test_merchant_registration(rf):
    url = reverse('merchant_register')
    data = {'username': 'newmerchant', 'password': 'securepass123', 'phone': '98765432101', 'userType': '2'}
    request = rf.post(url, data)
    add_session_to_request(request)
    response = merchant_register(request)
    assert response.status_code == 200
    assert Merchant.objects.filter(username='newmerchant').exists()


# test register for merchant with invalid data
@pytest.mark.django_db
def test_merchant_registration_with_invalid_data(rf):
    url = reverse('merchant_register')
    data = {'username': '', 'password': 'pass', 'phone': 'notaphone', 'userType': '2'}
    request = rf.post(url, data)
    add_session_to_request(request)
    response = merchant_register(request)
    assert response.status_code == 400  # Assuming the view returns 400 for invalid data
    assert not Merchant.objects.filter(username='').exists()


# test login of customer
@pytest.mark.django_db
def test_login_customer(rf):
    # Setup - create a user first
    Customer.objects.create(username='testuser', password='testpass')
    url = reverse('login_customer')
    data = {'username': 'testuser', 'password': 'testpass', 'userType': '1'}
    request = rf.post(url, data)
    add_session_to_request(request)
    response = login_customer(request)
    assert response.status_code == 200
    assert request.session['username'] == 'testuser'


@pytest.mark.django_db
def test_login_customer_with_wrong_password(rf):
    Customer.objects.create(username='testuser', password='rightpass')
    url = reverse('login_customer')
    data = {'username': 'testuser', 'password': 'wrongpass', 'userType': '1'}
    request = rf.post(url, data)
    add_session_to_request(request)
    response = login_customer(request)
    assert response.status_code == 400
    assert 'username' not in request.session


# test logout function
@pytest.mark.django_db
def test_logout(rf):
    url = reverse('logout')
    request = rf.get(url)
    add_session_to_request(request)
    request.session['username'] = 'testuser'
    response = logout_view(request)
    assert response.status_code == 302
    assert 'username' not in request.session




