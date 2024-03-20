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


# upload cart item
# def upload_cart(request):
#     if request.method == 'POST':
#         username = request.session.get('username', None) # customer name
#         user_type = request.session.get('user_type', None)
#         if username is None:
#             return JsonResponse({'message': 'Unauthorized access'}, status=401)
#         # verify the user type is customer
#         if not username or user_type != '1':
#             logout_view(request)
#             return JsonResponse({'error': 'Error user type or not logged in'}, status=400)
#
#         # TODO: 接收前端传来的products的列表与shop name
#         # TODO: 先通过username在ShoppingCart查找对应的cart，以及通过shop_name在Shop表格中查找对应的shop（这里记为t_shop）
#         # TODO: 然后使用cart在CartItem表格中查找对应的所有cartItem，并通过cartItem找出对应的product
#         # TODO: 然后筛选出这些product中属t_shop的所有product（满足这些条件的product记为t_product）
#         # TODO: 检查出cartItem中对应含有t_product的数据
#         '''
#         TODO:
#         1.若传来的的products列表中与cartItem中有对应的t_product，则检查该cartItem的quantity与products中对应的quantity是否相同，
#         若quantity相同则忽略，若不相同则用products中对应的quantity来覆盖cartItem中的值。
#
#         2.若传来的的products列表中没有一种product，而cartItem中有对应的t_product，则删除该cartItem数据
#
#         3.若传来的的products列表中有一种product，而cartItem中没有对应的t_product，则创建cartItem来记录
#         '''
#         # TODO:注意错误处理
#         return
#     return

# upload cart item info
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

    print("request method = get")
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


# gets all the user's cartItem, cart界面使用该方法
def get_cart(request):
    if request.method == 'POST':
        username = request.session.get('username', None)
        user_type = request.session.get('user_type', None)
        if username is None:
            return JsonResponse({'message': 'Unauthorized access'}, status=401)
        if username is None:
            return JsonResponse({'message': 'Unauthorized access'}, status=401)
        # verify the user type is customer
        if not username or user_type != '1':
            logout_view(request)
            return JsonResponse({'error': 'Error user type or not logged in'}, status=400)

        try:
            customer = Customer.objects.get(username=username)
            cart = ShoppingCart.objects.filter(customer=customer).first()

            if cart:
                cart_items = CartItem.objects.filter(cart=cart)
                products_list = [{'id': item.product.id, 'name': item.product.name, 'price': item.product.price, 'quantity': item.product.quantity} for
                                 item in cart_items]
                return JsonResponse({'products': products_list})
            else:
                return JsonResponse({'message': 'Cart not found'}, status=404)

        except Customer.DoesNotExist:
            return JsonResponse({'message': 'Customer does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
