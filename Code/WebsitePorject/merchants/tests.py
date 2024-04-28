from decimal import Decimal
from PIL import Image
from io import BytesIO
from django.core.files.images import ImageFile
import pytest
from django.urls import reverse
from django.test import RequestFactory
from accounts.models import Shop, Merchant
from merchants.models import Product
from django.contrib.sessions.middleware import SessionMiddleware
from merchants.views import new_store, add_product, modify_product, delete_product


# Helper to add session middleware to requests
def add_session_to_request(request):
    middleware = SessionMiddleware(lambda x: x)
    middleware.process_request(request)
    request.session.save()


# create a instance of image
def create_image_file():
    file = BytesIO()
    image = Image.new('RGB', (100, 100), color='red')
    image.save(file, 'PNG')
    file.name = 'test.png'
    file.seek(0)
    return ImageFile(file)


@pytest.fixture
def rf():
    return RequestFactory()


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
        price=Decimal("19.99"),
        description="Test Description",
        category="TestCategory",
        shop=shop,
        image_path="/path/to/image"
    )


@pytest.mark.django_db
def test_create_shop(rf):
    merchant2 = Merchant.objects.create(username='TestMerchant2', password='password123456', phone_number='22345678901')
    request = rf.post(reverse('new_store'), data={
        'name': 'TestStore2',
        'province': 'TestProvince',
        'city': 'TestCity',
        'district': 'TestD',
        'detail': 'TestDetail',
        'storeImage': create_image_file()
    })
    add_session_to_request(request)
    request.session['username'] = merchant2.username
    request.session['user_type'] = '2'
    request.user = merchant2
    response = new_store(request)
    assert response.status_code == 302
    assert Shop.objects.filter(name='TestStore2').exists()


@pytest.mark.django_db
def test_add_product(rf, merchant, shop):
    print("shop name=",merchant.shop.name)
    request = rf.post(reverse('add_product'), data={
        'name': 'New Product',
        'price': '19.99',
        'description': 'A new product description',
        'category': 'General',
        'productImage': create_image_file()
    })
    add_session_to_request(request)
    request.session['username'] = merchant.username
    request.user = merchant
    response = add_product(request)
    assert response.status_code == 200
    assert Product.objects.filter(name='New Product', shop=shop).exists()


@pytest.mark.django_db
def test_modify_product(rf, merchant, product):
    request = rf.post(reverse('modify_product'), data={
        'id': product.id,
        'name': 'Updated Product',
        'price': '29.99'
    })
    add_session_to_request(request)
    request.session['username'] = merchant.username
    request.session['user_type'] = '2'
    request.user = merchant
    response = modify_product(request)
    assert response.status_code == 200
    product.refresh_from_db()
    assert product.name == 'Updated Product'
    assert product.price == Decimal('29.99')


@pytest.mark.django_db
def test_delete_product(rf, merchant, product):
    request = rf.post(reverse('delete_product'), data={
        'id': product.id
    })
    add_session_to_request(request)
    request.session['username'] = merchant.username
    request.user = merchant
    response = delete_product(request)
    assert response.status_code == 200
    with pytest.raises(Product.DoesNotExist):
        Product.objects.get(id=product.id)


@pytest.mark.django_db
def test_delete_non_existing_product(rf, merchant):
    request = rf.post(reverse('delete_product'), data={
        'id': 9999 # assume this product is not exist
    })
    add_session_to_request(request)
    request.session['username'] = merchant.username
    request.user = merchant
    response = delete_product(request)
    assert response.status_code == 404

