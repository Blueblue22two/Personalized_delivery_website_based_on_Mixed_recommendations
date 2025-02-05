from decimal import Decimal, InvalidOperation
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from accounts.models import Merchant, Shop, Favorite
from merchants.models import Product, ShopRating
from orders.models import Order, OrderItem
from django.db.models import Sum, Avg
import os
from django.conf import settings
import shutil


# -- My store --
def my_store(request):
    username = request.session.get('username', None)
    user_type = request.session.get('user_type', None)  # if not exist then return none
    print("-- my store --")
    print("user_type: ", user_type)
    print("username: ", username)

    if username is None:
        return JsonResponse({'error': 'Unauthorized access'}, status=401)

    if user_type != '2':  # if user type != merchant
        print("Error user type!")
        logout_view(request)

    try:
        merchant = Merchant.objects.get(username=username)
    except Merchant.DoesNotExist:
        print("Error: merchant does not exist")
        return logout_view(request)

    shop = merchant.shop

    # upload rate
    if not upload_rate(request):
        print("upload rate failed")

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

        store_name = request.POST.get('name')
        store_image = request.FILES.get('storeImage', None)
        province = request.POST.get('province')
        city = request.POST.get('city')
        district = request.POST.get('district')
        detail = request.POST.get('detail')
        address = f'{province}-{city}-{district}-{detail}'
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

        # get the database file path
        dataset_base_dir = os.path.join(settings.BASE_DIR, 'Dataset')
        store_dir = os.path.join(dataset_base_dir, store_name.replace(" ", "_"))

        # Paths for 'LOGO' and 'Products' directories within the store directory
        logo_dir = os.path.join(store_dir, 'LOGO')
        products_dir = os.path.join(store_dir, 'Products')
        image_dir = os.path.join(logo_dir, store_image.name)

        # Create the directories if they do not already exist
        for directory in [store_dir, logo_dir, products_dir]:
            os.makedirs(directory, exist_ok=True)

        # store
        shop = Shop.objects.create(
            merchant=merchant,
            name=store_name,
            province=province,
            city=city,
            district=district,
            detail=detail,
            address=address,
            total_rating=0,  # default value
            image_path=os.path.relpath(image_dir, start=dataset_base_dir)
        )

        with open(os.path.join(logo_dir, store_image.name), 'wb+') as destination:
            for chunk in store_image.chunks():
                destination.write(chunk)

        merchant.shop = shop
        merchant.save()
        shop.save()
        print(f"Store {store_name} created successfully")
        return redirect(my_store)

    # if request != post, return error
    return render(request, 'create_store.html')


# add product view
def add_product(request):
    if request.method == 'POST':
        username = request.session.get('username', None)
        if username is None:
            return JsonResponse({'error': 'Unauthorized access'}, status=401)

        try:
            merchant = Merchant.objects.get(username=username)
            shop = Shop.objects.get(merchant=merchant)
            if shop is None:
                return JsonResponse({'error': 'Shop does not exist for this merchant'}, status=404)
        except Merchant.DoesNotExist:
            return JsonResponse({'error': 'Merchant does not exist'}, status=404)

        name = request.POST.get('name')  # product name
        price = request.POST.get('price')
        description = request.POST.get('description')
        category = request.POST.get('category')
        product_image = request.FILES.get('productImage')
        # Validation
        if not all([name, price, description, category, product_image]):
            return JsonResponse({'error': 'Missing data'}, status=400)
        try:
            price = Decimal(price)
            if price <= 0:
                return JsonResponse({'error': 'Price must be greater than zero'}, status=400)
            # check the image file
            if not product_image.name.endswith(('.png', '.jpg', '.jpeg')):
                return JsonResponse({'error': 'Invalid file type'}, status=400)
            # check same product name
            if Product.objects.filter(shop=shop, name=name).exists():
                print(f"Product with this name {name} already exists in your shop")
                return JsonResponse({'error': 'Product with this name already exists in your shop'}, status=409)
        except InvalidOperation:
            return JsonResponse({'error': 'Invalid price format'}, status=400)

        #  Dataset path
        dataset_base_dir = os.path.join(settings.BASE_DIR, 'Dataset')
        shop_path = os.path.join(dataset_base_dir, shop.name.replace(" ", "_"))  # use shop name
        # Check if shop_path exists, if not return an error or create it based on your requirement
        if not os.path.exists(shop_path):
            return JsonResponse({'error': 'Shop directory does not exist'}, status=404)

        #  Product path
        products_path = os.path.join(shop_path, 'Products')
        # Ensure the 'Products' directory exists under the shop directory
        if not os.path.exists(products_path):
            os.makedirs(products_path, exist_ok=True)
        product_folder_path = os.path.join(products_path, name.replace(" ", "_"))

        # create a product file
        os.makedirs(product_folder_path, exist_ok=True)
        image_file_path = os.path.join(product_folder_path, product_image.name)
        # save image in product file
        try:
            with open(image_file_path, 'wb+') as destination:
                for chunk in product_image.chunks():
                    destination.write(chunk)
        except IOError as e:
            return JsonResponse({'error': 'Failed to save image'}, status=500)

        product = Product(
            shop=shop,
            name=name,
            price=price,
            category=category,
            description=description,
            image_path=os.path.relpath(image_file_path, start=dataset_base_dir)
        )
        product.save()
        print("add product successfully")
        return JsonResponse({'message': 'add Product successfully', 'redirect_url': '/merchants/my_store/'},
                            status=200)
    else:
        return render(request, 'add_product.html')


# return all the product info in this store
def show_product(request):
    username = request.session.get('username', None)
    if username is None:
        return JsonResponse({'error': 'Unauthorized access'}, status=401)

    try:
        merchant = Merchant.objects.get(username=username)
        shop = merchant.shop
        products = Product.objects.filter(shop=shop).values('id', 'name', 'price', 'category', 'image_path')

        return JsonResponse(list(products), safe=False)
    except Merchant.DoesNotExist:
        return JsonResponse({'error': 'Merchant not found or does not have a shop'}, status=404)


# -- modify product page, receive modify data and store it --
def modify_product(request):
    username = request.session.get('username', None)  # merchant name
    if username is None:
        logout_view()
        return JsonResponse({'error': 'Unauthorized access'}, status=401)
    print("modify function...")

    if request.method == 'POST':
        product_id = request.POST.get('id')
        new_name = request.POST.get('name')
        new_price = request.POST.get('price')
        try:
            product = Product.objects.get(id=product_id, shop__merchant__username=username)
            old_path = os.path.join(settings.BASE_DIR, 'Dataset', product.shop.name.replace(" ", "_"), 'Products',
                                    product.name.replace(" ", "_"))
            new_path = os.path.join(settings.BASE_DIR, 'Dataset', product.shop.name.replace(" ", "_"), 'Products',
                                    new_name)

            # Rename the product folder if it exists
            if os.path.exists(old_path):
                os.rename(old_path, new_path)

            # Update product image_path
            if product.image_path:
                file_name = os.path.basename(product.image_path)  # Extracts file name
                print(f"file_name: {file_name}")
                new_image_path = os.path.join('Products', new_name, file_name)  # Constructs new relative path
                print(f"new_image_path: {new_image_path}")
                product.image_path = new_image_path

            # Update product information in the database
            product.name = new_name
            product.price = Decimal(new_price)
            product.save()

            print("Product updated successfully")
            return JsonResponse({'message': 'Product updated successfully'})
        except (ObjectDoesNotExist, InvalidOperation):
            print("Product not found or invalid input")
            return JsonResponse({'error': 'Product not found or invalid input'}, status=404)
    else:

        print("redirect to modification page")
        return render(request, 'modification.html')


# -- delete product --
def delete_product(request):
    username = request.session.get('username', None)
    if username is None:
        logout_view(request)
        return JsonResponse({'error': 'Unauthorized access'}, status=401)

    if request.method == 'POST':
        product_id = request.POST.get('id')
        try:
            product = Product.objects.get(id=product_id, shop__merchant__username=username)
            product_folder_path = os.path.join(settings.BASE_DIR, 'Dataset', product.shop.name.replace(" ", "_"),
                                               'Products', product.name.replace(" ", "_"))
            # shutil.rmtree() to delete all file of product
            if os.path.exists(product_folder_path):
                shutil.rmtree(product_folder_path)
            product.delete()
            return JsonResponse({'message': 'Product removed successfully'})
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)


# -- Promotion (optional) --
def promote_product(request):
    return


# -- get the store info --
def get_info(request):
    username = request.session.get('username', None)
    if username is None:
        print("Not log in")
        logout_view(request)

    try:
        merchant = Merchant.objects.get(username=username)
        shop = merchant.shop
        if not shop:
            return JsonResponse({'error': 'Shop not found'}, status=404)

        # get total_sales:
        total_sales = OrderItem.objects.filter(order__shop=shop).aggregate(Sum('quantity'))['quantity__sum'] or 0

        # get store total income
        total_income = Order.objects.filter(merchant=merchant).aggregate(Sum('total_price'))['total_price__sum'] or 0

        # get top product
        top_selling_product_info = OrderItem.objects.filter(order__shop=shop) \
            .values('product__id', 'product__name') \
            .annotate(total_sold=Sum('quantity')) \
            .order_by('-total_sold') \
            .first()

        top_product_name = top_selling_product_info['product__name'] if top_selling_product_info else 'None'
        top_product_id = top_selling_product_info['product__id'] if top_selling_product_info else None

        # Calculate average rate
        average_rate = ShopRating.objects.filter(shop=shop).aggregate(Avg('rate'))['rate__avg'] or 0

        # Calculate total number of orders for the shop
        order_number = Order.objects.filter(shop=shop).count()

        # Calculate how many times the shop has been favorited
        fav_number = Favorite.objects.filter(shop=shop).count()
        print(f"store name:{shop.name}, rate:{average_rate}")
        print(f"total income: {total_income}, total sales: {total_sales}")
        data = {
            'storeName': shop.name,
            'address': shop.address,
            'phone': merchant.phone_number,
            'rate': round(average_rate, 1),  # Round to 1 decimal places
            'totalIncome': total_income,
            'favNumber': fav_number,
            'orderNumber': order_number,
            'totalSales': total_sales,
            'totalProducts': shop.products.count(),
            'topSellingProduct': top_product_name,
            'topSellingProductId': top_product_id
        }
        # upload the shop rate
        if not upload_rate(request):
            print("upload rate failed")
        return JsonResponse(data, status=200)
    except Merchant.DoesNotExist:
        return JsonResponse({'error': 'Merchant not found'}, status=404)


# -- upload shop rate --
def upload_rate(request):
    print("upload rate function working...")
    username = request.session.get('username', None)  # merchant username
    if username is None:
        print("Not login")
        return False

    try:
        merchant = Merchant.objects.get(username=username)
        if merchant.shop is None:
            return False

        # Calculate average rate
        average_rate = ShopRating.objects.filter(shop=merchant.shop).aggregate(Avg('rate'))['rate__avg']
        print(f"average_rate: {average_rate}")
        if average_rate is not None:
            merchant.shop.total_rating = Decimal(average_rate).quantize(Decimal('0.1'))
            merchant.shop.save()
            print("Shop rating updated successfully")
            return True
        else:
            return False
    except Merchant.DoesNotExist:
        return False
