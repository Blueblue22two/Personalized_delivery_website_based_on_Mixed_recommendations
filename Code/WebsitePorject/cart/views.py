import json
from django.contrib.auth import logout
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from accounts.models import Customer, ShoppingCart, Shop
from cart.models import CartItem
from merchants.models import Product


# -- logout(clear session) & redirect to main page--
def logout_view(request):
    print("-- log out --")
    logout(request)
    print("log out successfully")
    return HttpResponseRedirect('/')


# Create your views here.
def main_page(request):
    return render(request, 'cart.html')


# upload data and store orders
def cart_info(request):
    if request.method == 'POST':
        # TODO:用户点击Pay后，receive the order data, and store it in orders
        # TODO:获取session中的username与user type，然后验证数据
        # TODO:返回结果
        return
    else:
        # TODO:返回 cart中的商品信息与对应的store信息到前端
        return


# upload cart item info from cart page
def upload(request):
    if request.method == 'POST':
        username = request.session.get('username', None) # customer username
        if username is None:
            return JsonResponse({'message': 'Unauthorized access'}, status=401)

        user_type = request.session.get('user_type', None)
        if not username or user_type != '1':
            return JsonResponse({'error': 'Error user type or not logged in'}, status=400)

        # TODO:获取前端传来的products列表
        data = json.loads(request.body.decode('utf-8'))
        products_data = data.get('products', [])
        print(f"upload_cart function: username: {username}")

        try:
            # TOOD:通过username获取Customer表格中对应的customer，然后通过customer获取shoppingcart
            customer = Customer.objects.get(username=username)
            cart, created = ShoppingCart.objects.get_or_create(customer=customer)

            return JsonResponse({'message': 'Cart updated successfully'})

        except Customer.DoesNotExist:
            return JsonResponse({'error': 'Customer not found'}, status=404)
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=400)


# upload cart item info from store page
def upload_cart(request):
    if request.method == 'POST':
        username = request.session.get('username', None) # customer username
        if username is None:
            return JsonResponse({'message': 'Unauthorized access'}, status=401)

        user_type = request.session.get('user_type', None)
        if not username or user_type != '1':
            return JsonResponse({'error': 'Error user type or not logged in'}, status=400)

        # Decode the request body
        data = json.loads(request.body.decode('utf-8'))
        shop_name = data.get('shopName', '')
        products_data = data.get('products', [])
        print(f"upload_cart function:  shop_name: {shop_name}, username: {username}")

        try:
            customer = Customer.objects.get(username=username)
            shop = Shop.objects.get(name=shop_name)
            cart, created = ShoppingCart.objects.get_or_create(customer=customer)

            # 获取当前商店的所有产品ID
            product_ids = [product['id'] for product in products_data]
            shop_products = Product.objects.filter(id__in=product_ids, shop=shop)

            # 更新或创建CartItem
            for product_data in products_data:
                product_id = product_data['id']
                quantity = product_data['quantity']
                product = shop_products.get(id=product_id)
                CartItem.objects.update_or_create(cart=cart, product=product, defaults={'quantity': quantity})

            # 删除不存在于products_data中的CartItem
            CartItem.objects.filter(cart=cart, product__in=shop_products).exclude(product__id__in=product_ids).delete()

            return JsonResponse({'message': 'Cart updated successfully'})

        except Customer.DoesNotExist:
            return JsonResponse({'error': 'Customer not found'}, status=404)
        except Shop.DoesNotExist:
            return JsonResponse({'error': 'Shop not found'}, status=404)
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=400)


# get a cart item of a store
def get_cart_store(request):
    if request.method == 'POST':
        username = request.session.get('username', None)
        user_type = request.session.get('user_type', None)
        if username is None:
            return JsonResponse({'message': 'Unauthorized access'}, status=401)
        # verify the user type is customer
        if not username or user_type != '1':
            logout_view(request)
            return JsonResponse({'error': 'Error user type or not logged in'}, status=400)

        # get the shop name
        shop_name = request.POST.get('shopName')
        print(f"get_cart_store >: shop name: {shop_name}")

        try:
            customer = Customer.objects.get(username=username)
            shop = Shop.objects.get(name=shop_name)
            cart = ShoppingCart.objects.filter(customer=customer).first()

            if cart:
                cart_items = CartItem.objects.filter(cart=cart, product__shop=shop)
                products_list = [{'id': item.product.id, 'name': item.product.name, 'price': item.product.price,
                                  'quantity': item.quantity} for item in cart_items]
                return JsonResponse({'products': products_list})
            else:
                return JsonResponse({'message': 'Cart not found'}, status=404)

        except Customer.DoesNotExist:
            return JsonResponse({'message': 'Customer does not exist'}, status=404)
        except Shop.DoesNotExist:
            return JsonResponse({'message': 'Shop does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)


# gets all the user's cartItem
def get_cart(request):
    username = request.session.get('username', None)
    user_type = request.session.get('user_type', None)
    if username is None:
        return JsonResponse({'message': 'Unauthorized access'}, status=401)
    # verify the user type is customer
    if not username or user_type != '1':
        logout_view(request)
        return JsonResponse({'error': 'Error user type or not logged in'}, status=400)
    print("get_cart function...")
    try:
        customer = Customer.objects.get(username=username)
        cart = ShoppingCart.objects.filter(customer=customer).first()

        if cart:
            cart_items = CartItem.objects.filter(cart=cart)
            products_list = [{'id': item.product.id, 'name': item.product.name, 'price': item.product.price, 'quantity': item.quantity} for
                             item in cart_items]
            return JsonResponse({'products': products_list})
        else:
            return JsonResponse({'message': 'Cart not found'}, status=404)

    except Customer.DoesNotExist:
        return JsonResponse({'message': 'Customer does not exist'}, status=404)
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=500)
