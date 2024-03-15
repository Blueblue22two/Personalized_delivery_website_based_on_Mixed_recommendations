from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from accounts.models import Merchant, Shop
import os
from django.conf import settings


# Create your views here.

# -- My store --
def my_store(request):
    username = request.session.get('username', None)
    user_type = request.session.get('user_type', None) # if not exist then return none
    print("-- my store --")
    print("user_type: ", user_type)
    print("username: ",username)

    if user_type != '2':  # if user type != merchant
        print("Error user type!")
        logout_view(request)

    try:
        merchant = Merchant.objects.get(username=username)
    except Merchant.DoesNotExist:
        print("Error: merchant does not exist")
        return logout_view(request)

    shop = merchant.shop
    if not shop:
        # If the merchant does not have an associated shop, direct them to create one
        print("The user has not registered a store")
        return redirect('new_store')
    else:
        # If a shop exists, pass the shop object to the template for rendering
        return render(request, 'my_store.html')


# -- logout(clear session) & redirect to main page--
def logout_view(request):
    print("-- log out --")
    logout(request)
    print("log out successfully")
    return HttpResponseRedirect('/')


# register a new store for a new merchant
def new_store(request):
    if request.method == 'POST':
        username = request.session.get('username', None)
        user_type = request.session.get('user_type', None)  # if not exist then return none
        store_name= request.POST.get('name')
        store_image = request.FILES.get('storeImage', None)
        address = request.POST.get('address')

        print("-- new store --")
        print("Username:", username)
        print("User Type:", user_type)
        print("Store Name:", store_name)
        print("Address:", address)

        if not username or user_type != '2':
            logout_view(request)
            return JsonResponse({'error': 'Error user type or not logged in'}, status=400)

        if store_image is None:
            return JsonResponse({'error': 'No image uploaded'}, status=400)

        # Checks if the merchant exists
        try:
            merchant = Merchant.objects.get(username=username)
        except Merchant.DoesNotExist:
            logout_view(request)
            return JsonResponse({'error': 'Merchant not found'}, status=404)

        # Check if there is a store with the same name
        if Shop.objects.filter(name=store_name).exists():
            return JsonResponse({'error': 'Store name already exists'}, status=400)

        # Calculate the path to the 'Dataset' directory
        dataset_base_dir = os.path.join(settings.BASE_DIR, '..', 'Dataset')
        store_dir = os.path.join(dataset_base_dir, store_name)

        # Paths for 'LOGO' and 'Products' directories within the store directory
        logo_dir = os.path.join(store_dir, 'LOGO')
        products_dir = os.path.join(store_dir, 'Products')

        # Create the directories if they do not already exist
        for directory in [store_dir, logo_dir, products_dir]:
            os.makedirs(directory, exist_ok=True)

        # store
        shop = Shop.objects.create(
            merchant=merchant,
            name=store_name,
            address=address,
            total_rating=0,  # default value
            image_path=os.path.join(logo_dir, store_image.name) # store the path of image
        )

        with open(os.path.join(logo_dir, store_image.name), 'wb+') as destination:
            for chunk in store_image.chunks():
                destination.write(chunk)

        merchant.shop = shop
        merchant.save()
        shop.save()
        print(f"Store {store_name} created successfully")
        # redirect_url = '/merchants/my_store/'
        # response = JsonResponse({'message': 'Store created successfully', 'redirect_url': redirect_url},
        #                         status=200)
        return redirect(my_store)

    # if request != post, return error
    return render(request, 'create_store.html')


# -- add product --
def add_product(request):
    if request.method == 'POST':
        # TODO: receive data and store it
        return
    return render(request, '.html')


# -- modify product --
def modify_product(request):
    if request.method == 'POST':
        # TODO: receive data and store it
        return
    return render(request, '.html')


# -- show product --
def show_product(request):
    # TODO: return all the products info in this store
    return


# -- upload shop rate --
def upload_rate(request):
    # 在其他函数中调用这个函数
    # TODO:获取session username，查询mysql中对应的merchants，然后查询其shop_id
    # TODO:通过shop_id查询表格 ShopRatings中所有对应shop_id的数据，然后求和再求平均数
    # TODO:得到平均数后将数据更新到对应的Shops表格的数据中
    return
