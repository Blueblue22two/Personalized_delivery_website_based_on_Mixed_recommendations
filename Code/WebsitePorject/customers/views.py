from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from accounts.models import Customer, Shop, Favorite


# Create your views here.


# user profile page (optional)
from customers.models import FavItem
from merchants.models import Product


def profile(request):
    return render(request, 'profile.html')


# user favorite
def fav(request):
    return render(request, 'fav.html')


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
        print("add_fav working...")
        username = request.session.get('username', None) # customer name
        if username is None:
            return JsonResponse({'message': 'Unauthorized access'}, status=401)

        # get the product id
        product_id = request.POST.get('productId')
        try:
            customer = Customer.objects.get(username=username)
            product = Product.objects.get(id=product_id)

            # 检查是否已经添加到收藏
            if FavItem.objects.filter(customer=customer, product=product).exists():
                return JsonResponse({'message': 'You have already added this product to favorites.'}, status=400)

            # 添加到收藏
            FavItem.objects.create(customer=customer, product=product)
            return JsonResponse({'message': 'Product added to favorites successfully!'})

        except Customer.DoesNotExist:
            return JsonResponse({'message': 'Customer not found'}, status=404)
        except Product.DoesNotExist:
            return JsonResponse({'message': 'Product not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=400)