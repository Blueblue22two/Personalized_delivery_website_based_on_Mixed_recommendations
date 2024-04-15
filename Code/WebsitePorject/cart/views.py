import json
from django.contrib.auth import logout
from django.db import IntegrityError, transaction
from django.core.exceptions import ValidationError
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
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


# add product to cart#
def add_cart(request):
    if request.method == 'POST':
        username = request.session.get('username', None)
        if username is None:
            return JsonResponse({'message': 'Unauthorized access'}, status=401)
        user_type = request.session.get('user_type', None)
        if not username or user_type != '1':
            return JsonResponse({'error': 'Error user type or not logged in'}, status=400)
        product_id = request.POST.get('productId')

        try:
            customer = Customer.objects.get(username=username)
            shopping_cart = get_object_or_404(ShoppingCart, customer=customer)
            product = get_object_or_404(Product, pk=product_id)
            cart_item, created = CartItem.objects.get_or_create(
                cart=shopping_cart,
                product=product,
                defaults={'quantity': 1}
            )
            if not created:
                cart_item.quantity += 1
            cart_item.save()
            return JsonResponse({'message': f'Product {product_id} added to cart successfully.'})

        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product does not exist'}, status=404)
        except Customer.DoesNotExist:
            return JsonResponse({'error': 'Customer does not exist'}, status=404)
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            return JsonResponse({'error': str(e)}, status=500)
    print(" add_cart function,request method != post")
    return JsonResponse({'error': 'Invalid request'}, status=400)


# upload cart item info from cart page
def upload(request):
    if request.method == 'POST':
        username = request.session.get('username', None)
        if username is None:
            return JsonResponse({'message': 'Unauthorized access'}, status=401)

        user_type = request.session.get('user_type', None)
        if not username or user_type != '1':
            return JsonResponse({'error': 'Error user type or not logged in'}, status=400)

        data = json.loads(request.body.decode('utf-8'))
        products_data = data.get('products', [])
        print(f"upload_cart function: username: {username}")

        try:
            # Fetching the Customer object
            customer = Customer.objects.get(username=username)
            # Retrieving the ShoppingCart object, create if not exist
            shopping_cart, _ = ShoppingCart.objects.get_or_create(customer=customer)
            # Fetching all CartItems for the customer's shopping cart
            existing_cart_items = CartItem.objects.filter(cart=shopping_cart)

            # Start database transaction
            with transaction.atomic():
                # Product IDs in the request
                product_ids = [item['id'] for item in products_data]

                # Update existing or create new CartItems
                for product_data in products_data:
                    product_id = product_data['id']
                    quantity = product_data['quantity']

                    # Fetch or create the Product object
                    product, _ = Product.objects.get_or_create(id=product_id)

                    # Update or create CartItem
                    cart_item, created = CartItem.objects.update_or_create(
                        cart=shopping_cart,
                        product=product,
                        defaults={'quantity': quantity}
                    )

                # Remove CartItems not in the products_data
                existing_cart_items.exclude(product__id__in=product_ids).delete()

            return JsonResponse({'message': 'Cart updated successfully'},status=200)

        except Customer.DoesNotExist:
            return JsonResponse({'error': 'Customer not found'}, status=404)
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)
        except IntegrityError as e:
            return JsonResponse({'error': str(e)}, status=500)
        except Exception as e:
            print(str(e))
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

            # get al pid in this store
            product_ids = [product['id'] for product in products_data]
            shop_products = Product.objects.filter(id__in=product_ids, shop=shop)

            # update ot create CartItem
            for product_data in products_data:
                product_id = product_data['id']
                quantity = product_data['quantity']
                product = shop_products.get(id=product_id)
                CartItem.objects.update_or_create(cart=cart, product=product, defaults={'quantity': quantity})

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
