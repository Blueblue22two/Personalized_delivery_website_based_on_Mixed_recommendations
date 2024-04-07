from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from accounts.models import Customer, Shop, Favorite, Address
from customers.models import FavItem
from merchants.models import Product

# Create your views here.


# customer favorite page
def fav(request):
    return render(request, 'favorites.html')


def cancel_product_fav(request, id):
    username = request.session.get('username', None)
    user_type = request.session.get('user_type', None)
    if username and user_type == '1':
        try:
            customer = Customer.objects.get(username=username)
            product = get_object_or_404(Product, pk=id)
            FavItem.objects.filter(customer=customer, product=product).delete()
            return JsonResponse({'message': 'Product favorite successfully cancelled.'})
        except Customer.DoesNotExist:
            return JsonResponse({'message': 'Customer does not exist.'}, status=404)
    else:
        return JsonResponse({'message': 'error: Non-existent user type.'}, status=400)


def cancel_shop_fav(request, name):
    username = request.session.get('username', None)
    user_type = request.session.get('user_type', None)
    if username and user_type == '1':
        try:
            customer = Customer.objects.get(username=username)
            shop = get_object_or_404(Shop, name=name)
            Favorite.objects.filter(user=customer, shop=shop).delete()
            return JsonResponse({'message': 'Shop favorite successfully cancelled.'})
        except Customer.DoesNotExist:
            return JsonResponse({'message': 'Customer does not exist.'}, status=404)
    else:
        return JsonResponse({'message': 'error: Non-existent user type.'}, status=400)


# add store to favorite
def add_fav(request):
    if request.method == 'POST':
        print("add_fav working...")
        username = request.session.get('username', None)
        if username is None:
            return JsonResponse({'message': 'Unauthorized access'}, status=401)

        # get the shop name
        shop_name = request.POST.get('shopName')
        print(f"shop name: {shop_name}")
        try:
            customer = Customer.objects.get(username=username)
            shop = Shop.objects.get(name=shop_name)
            # Check if the shop is already favorited
            if Favorite.objects.filter(user=customer, shop=shop).exists():
                return JsonResponse({'message': 'You have already added this shop to favorites.'})
            else:
                # Add to favorites if not already added
                Favorite.objects.create(user=customer, shop=shop)
                return JsonResponse({'message': 'Shop added to favorites successfully!'})

        except Customer.DoesNotExist:
            return JsonResponse({'message': 'Customer does not exist'}, status=404)
        except Shop.DoesNotExist:
            return JsonResponse({'message': 'Shop does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)


# add product to favorite
def add_fav_product(request):
    if request.method == 'POST':
        username = request.session.get('username', None)  # customer username
        if username is None:
            return JsonResponse({'message': 'Unauthorized access'}, status=401)

        user_type = request.session.get('user_type', None)
        if not username or user_type != '1':
            return JsonResponse({'error': 'Error user type or not logged in'}, status=400)

        # get the product id
        product_id = request.POST.get('productId')
        try:
            customer = Customer.objects.get(username=username)
            product = Product.objects.get(id=product_id)

            # 检查是否已经添加到收藏
            if FavItem.objects.filter(customer=customer, product=product).exists():
                return JsonResponse({'message': 'You have already added this product to favorites.'}, status=400)

            # add
            FavItem.objects.create(customer=customer, product=product)
            return JsonResponse({'message': 'Product added to favorites successfully!'})

        except Customer.DoesNotExist:
            return JsonResponse({'message': 'Customer not found'}, status=404)
        except Product.DoesNotExist:
            return JsonResponse({'message': 'Product not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=400)


# add a new address
def add_address(request):
    if request.method == 'POST':
        # customer username
        username = request.session.get('username', None)
        if username is None:
            return JsonResponse({'message': 'Unauthorized access'}, status=401)

        user_type = request.session.get('user_type', None)
        if not username or user_type != '1':
            return JsonResponse({'error': 'Error user type or not logged in'}, status=400)

        province = request.POST.get('province')
        city = request.POST.get('city')
        district= request.POST.get('district')
        detail = request.POST.get('detail')
        address_line = f'{province}-{city}-{district}-{detail}'  # Concatenate the address string

        try:
            customer = Customer.objects.get(username=username)
            new_address = Address(customer=customer, address_line=address_line, province=province, city=city,
                                  district=district, detail=detail)
            new_address.save()

            return redirect('/carts/main/')
        except Customer.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Customer does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return render(request, 'add_address.html')


# get all the address of this customer
def get_address(request):
    username = request.session.get('username', None)  # customer username
    if username is None:
        return JsonResponse({'message': 'Unauthorized access'}, status=401)

    user_type = request.session.get('user_type', None)
    if not username or user_type != '1':
        return JsonResponse({'error': 'Error user type or not logged in'}, status=400)

    try:
        customer = Customer.objects.get(username=username)
        addresses = Address.objects.filter(customer=customer)

        address_list = [{
            'id':address.id,
            'province': address.province,
            'city': address.city,
            'district': address.district,
            'detail': address.detail,
        } for address in addresses]

        return JsonResponse({'addresses': address_list})
    except Customer.DoesNotExist:
        return JsonResponse({'message': 'Customer does not exist'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)