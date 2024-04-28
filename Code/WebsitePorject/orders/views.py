import json
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from accounts.models import Customer, Merchant
from customers.models import Comment
from merchants.models import Product, ShopRating
from orders.models import Order, OrderItem


# redirect to my order page
def my_orders(request):
    return render(request, "my_order.html")


# get all the order info (My order page)
def get_order(request):
    username = request.session.get('username', None)
    if username is None:
        return JsonResponse({'message': 'Unauthorized access'}, status=401)
    user_type = request.session.get('user_type', None)

    if user_type in ['1', '2']:
        try:
            if user_type == '1':
                # for customer
                customer = Customer.objects.get(username=username)
                orders = Order.objects.filter(customer=customer).order_by('-id')
            else:
                # for merchant
                merchant = Merchant.objects.get(username=username)
                orders = Order.objects.filter(merchant=merchant).order_by('-id')

            order_data = [] # store all order data
            for order in orders:
                order_items = OrderItem.objects.filter(order=order)
                order_item_data = []
                for order_item in order_items:
                    product = order_item.product
                    order_item_data.append({
                        'product_name': product.name,
                        'product_price': order_item.product_price,
                        'quantity': order_item.quantity
                    })
                shop = order.shop

                order_data.append({
                    'order_id': order.id,
                    'total_price': order.total_price,
                    'sale_time': order.sale_time,
                    'payment_status': order.payment_status,
                    'delivery_status': order.delivery_status,
                    'isComment': order.isComment,
                    'order_items': order_item_data,
                    'address_line': order.address_line, # customer address
                    'shop_name': shop.name,
                    'shop_image_path': shop.image_path,
                    'shop_address': shop.address
                })
            return JsonResponse({
                'orders': order_data,
                'user_type': user_type
            })
        except Customer.DoesNotExist:
            return JsonResponse({'error': 'Customer does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Error user type or not logged in'}, status=400)


# set the order status to 'completed', only for merchant user to delivery fod
def send_order(request):
    if request.method == 'POST':
        username = request.session.get('username', None)
        if username is None:
            return JsonResponse({'message': 'Unauthorized access'}, status=401)

        user_type = request.session.get('user_type', None)
        if not username or user_type != '2':  # user type='2' stand for merchant user
            return JsonResponse({'error': 'Error user type or not logged in'}, status=400)

        # Extracting order_id from POST request data
        order_id = request.POST.get('order_id', None)
        print(f"order id:{order_id}")
        if order_id is None:
            return JsonResponse({'error': 'Order ID is missing'}, status=400)
        try:
            # Find the order with the given ID
            order = Order.objects.get(id=order_id, merchant__username=username)
            # Set the delivery status to True
            order.delivery_status = True
            order.save()
            return JsonResponse({'message': 'Order status updated successfully'}, status=200)

        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Order not found or you do not have permission to modify it'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)


# get the order info
def get_info(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        if not order_id:
            return JsonResponse({'error': 'Order ID is missing'}, status=400)
        try:
            order = get_object_or_404(Order, id=order_id)
            order_data = []

            order_info = {
                'total_price': order.total_price,
                'sale_time': order.sale_time.strftime('%Y-%m-%d %H:%M:%S'),  # 格式化日期时间
                'shop_name': order.shop.name,
                'shop_address': order.shop.address,
                'shop_image_path': order.shop.image_path,
                'order_items': []
            }

            order_items = OrderItem.objects.filter(order=order)
            for item in order_items:
                order_info['order_items'].append({
                    'product_name': item.product.name,
                    'product_price': item.product_price,
                    'quantity': item.quantity
                })
            order_data.append(order_info)
            return JsonResponse({'orders': order_data})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)


# receive the order info and rating, comment data and store it
def post_comment(request):
    if request.method == 'POST':
        username = request.session.get('username')
        if username is None:
            return JsonResponse({'error': 'Unauthorized access'}, status=401)
        user_type = request.session.get('user_type')
        if not username or user_type != '1':  # Assuming '1' is the user type for customers
            return JsonResponse({'error': 'Error user type or not logged in'}, status=400)

        # get json data
        data = json.loads(request.body.decode('utf-8'))
        order_id = data.get('order_id')
        shopRating = data.get('shopRating')
        commentText = data.get('commentText')
        productRatings = data.get('productRatings')
        print(f"order id:{order_id}")
        print(f"shopRating: {shopRating}")
        print(f"comment: {commentText}")
        print(f"productRating: {productRatings}")

        try:
            customer = get_object_or_404(Customer, username=username)
            order = get_object_or_404(Order, id=order_id, customer=customer)

            # create ShopRating object
            ShopRating.objects.create(shop=order.shop, rate=shopRating)
            # update store total rating
            new_total_rating = ShopRating.objects.filter(shop=order.shop).aggregate(Avg('rate'))['rate__avg']
            order.shop.total_rating = new_total_rating
            order.shop.save()
            # create comment
            for productRating in productRatings:
                product_name = productRating['name']
                rating = productRating['rating']
                try:
                    product = Product.objects.get(name=product_name, shop=order.shop)
                    Comment.objects.create(customer=customer, product=product, text=commentText, rating=rating)
                    # update product average rate
                    product.update_average_rate()
                except ObjectDoesNotExist:
                    print(f"Error: No product matches the given query for name {product_name} in shop {order.shop.name}")
                    return JsonResponse({'error': f"No product matches the given query for name {product_name}"}, status=400)

            # set the isComment=True
            order.isComment = True
            order.save()
            return JsonResponse({'success': True, 'redirect_url': '/orders/my_orders/'})
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)


# jump to the comment page with order id
def post_comment_view(request, id):
    # send order id
    context = {'order_id': id}
    print(f"order id: {id}")
    return render(request, 'comment.html', context)
