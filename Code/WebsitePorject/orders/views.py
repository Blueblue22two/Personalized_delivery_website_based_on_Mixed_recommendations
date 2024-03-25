from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from accounts.models import Customer
from customers.models import Comment
from merchants.models import Product, ShopRating
from orders.models import Order, OrderItem


def my_orders(request):
    return render(request, "my_order.html")


# get all the order info
def get_order(request):
    username = request.session.get('username', None)
    if username is None:
        return JsonResponse({'message': 'Unauthorized access'}, status=401)

    user_type = request.session.get('user_type', None)
    '''
        所有需要返回的数据:
        1. 对应的Order表格中的数据:order id, total_price， sale_time， payment_status， delivery_status, isComment
        2. 对应的OrderItem表格中的数据：product_price， quantity
        3. 对应的Product表格中的数据:name (代表product name)
        4. 对应的Shop表格中的数据:name (代表shop name), image_path, address
        5. user_type
    '''
    #  通过username在Customer表格中找到对应的customer
    #  通过customer在Order表格中找到所有对应的order数据,然后获取其order id, total_price， sale_time， payment_status， delivery_status，isComment
    #  通过order在OrderItem找到所有对应的orderItem数据，然后获取其product_price， quantity
    #  通过order中的外键shop，在Shop表格中找到对应的数据shop，然后获取其name, image_path, address
    #  通过orderItem中的product外键，在Product表格中找到对应的product数据，然后获取其name
    if user_type in ['1', '2']:  # user type exists
        try:
            customer = Customer.objects.get(username=username)
            orders = Order.objects.filter(customer=customer)
            order_data = []
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
                    'isComment': order.isComment,  # 添加isComment值
                    'order_items': order_item_data,
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


# set the order status to 'completed', only for merchant user
def send_order(request):
    if request.method == 'POST':
        username = request.session.get('username', None)
        if username is None:
            return JsonResponse({'message': 'Unauthorized access'}, status=401)

        user_type = request.session.get('user_type', None)
        if not username or user_type != '2': # user type='2' stand for merchant user
            return JsonResponse({'error': 'Error user type or not logged in'}, status=400)

        # Extracting order_id from POST request data
        order_id = request.POST.get('order_id', None)
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


# get the info from database
def get_info(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        if not order_id:
            return JsonResponse({'error': 'Order ID is missing'}, status=400)
        try:
            # 通过参数order_id在Order中找到对应的数据order
            order = get_object_or_404(Order, id=order_id)
            order_data = []  # 存储该订单的所有信息，然后传给前端

            # 将order中的数据total_price， sale_time保存
            order_info = {
                'total_price': order.total_price,
                'sale_time': order.sale_time.strftime('%Y-%m-%d %H:%M:%S'),  # 格式化日期时间
                'shop_name': order.shop.name,
                'shop_address': order.shop.address,
                'shop_image_path': order.shop.image_path,
                'order_items': []
            }

            # 通过order找到所有对应的OrderItem中的数据
            order_items = OrderItem.objects.filter(order=order)
            for item in order_items:
                # 通过OrderItem数据中的product外键找到Product表格中对应的数据，获取其name
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



# def post_comment(request):
#     if request.method == 'POST':
#         username = request.session.get('username', None)
#         if username is None:
#             return JsonResponse({'message': 'Unauthorized access'}, status=401)
#         user_type = request.session.get('user_type', None)
#         if not username or user_type != '1':  # user type='' stand for customer user
#             return JsonResponse({'error': 'Error user type or not logged in'}, status=400)
#
#         # TODO: 使用username在Customer表格中寻找对应的customer数据
#         # TODO: 接收前端传来的数据，利用其中的数据order id在Order中找到对应的数据order
#         # TODO: 将其中的comment数据保存到Comment与ShopRating表格中
#         # TODO: 在表格ShopRating创建数据，其中的数值rate 等于 传来的数据中的shopRating
#         # TODO: 根据传来的数据中的{name: productName, rating: productRating}与commentText，先用productName在Product表格中找到对应的product数据，然后在Comment表格中创建对应的数据
#         # TODO: 若前面的都存储成功后，将order中的数据isComment设置为True
#         # TODO: 注意错误处理
#         # TODO: 若成功则redirect to url='/orders/my_orders/'
#         return
#     else:
#         return JsonResponse({'error': 'Invalid request method.'}, status=400)

# 接收前端传来的评论与评分数据，然后操作
def post_comment(request):
    if request.method == 'POST':
        username = request.session.get('username')
        if username is None:
            return JsonResponse({'error': 'Unauthorized access'}, status=401)
        user_type = request.session.get('user_type')
        if not username or user_type != '1':  # Assuming '1' is the user type for customers
            return JsonResponse({'error': 'Error user type or not logged in'}, status=400)

        # get fromData
        order_id = request.POST.get('order_id')
        shopRating = request.POST.get('shopRating')
        commentText = request.POST.get('commentText')
        print(f"order id:{order_id}")
        print(f"shopRating: {shopRating}")

        customer = get_object_or_404(Customer, username=username)
        order = get_object_or_404(Order, id=order_id, customer=customer)
        try:
            # create ShopRating value
            ShopRating.objects.create(shop=order.shop, rate=shopRating)

            # 处理每个产品评分和评论
            productRatings = request.POST.getlist('productRatings[]')
            for productRating in productRatings:
                product_name = productRating['name']
                rating = productRating['rating']
                product = get_object_or_404(Product, name=product_name, shop=order.shop)
                Comment.objects.create(customer=customer, product=product, text=commentText, rating=rating)

            # set the isComment=True
            order.isComment = True
            order.save()
            return JsonResponse({'success': True, 'redirect_url': '/orders/my_orders/'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)


# jump to the comment page with order id
def post_comment_view(request, id):
    # 将order_id包装在字典中，作为上下文传递给模板
    context = {'order_id': id}
    print(f"order id: {id}")
    return render(request, 'comment.html', context)

