import json

from django.core.exceptions import ObjectDoesNotExist

from django.utils.timezone import now
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, redirect
from accounts.models import Customer, Address, Shop
from merchants.models import Product
from orders.models import Order, OrderItem


# Create your views here.
def payment(request):
    if request.method == 'POST':
        try:
            result = json.loads(request.POST.get('result'))
            orders = json.loads(request.POST.get('orders'))

            for order_data in orders:
                order_id = order_data.get('OrderId')
                Order.objects.filter(id=order_id).update(payment_status=result)

            return redirect('/orders/my_orders/')
        except Exception as e:
            print(e)
            return JsonResponse({'error': 'An error occurred during processing'}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)


# 接收前端传来的数据并为其生成order与order item
def generate_payment(request):
    if request.method == 'POST':
        username = request.session.get('username', None)
        if username is None:
            return JsonResponse({'message': 'Unauthorized access'}, status=401)
        user_type = request.session.get('user_type', None)
        if not username or user_type != '1':
            return JsonResponse({'error': 'Error user type or not logged in'}, status=400)
        print("function: generate_payment working...")
        try:
            total_price = request.POST.get('total_price')
            address_id = request.POST.get('address_id')
            products_data = json.loads(request.POST.get('products'))
            # get customer
            customer = Customer.objects.get(username=username)
            # get address
            address = Address.objects.get(id=address_id)
            address_line = address.address_line
            print(f"address id: {address_id}")
            print(f"address_line: {address_line}")

            # get time
            sale_time = now()
#         现在先创建一个List，其中存储的数据类型为{shopId,OrderId}，设这个List叫temp
#         现在在Products中有多个对象{productId, quantity}，以一个对象为例：
#         先使用对象中productId的在Product表格中寻找对应的product数据，获取其对应的price与外键shop
#         利用外键shop在Shop表格找到对应的数据shop然后获取其shop id
#         如果现在操作的这个数据获取到的shopId，遍历temp中的所有数据，如果找到有与之对应的shopId，则进行下面的操作分支B。若没有找到，则进行下面的操作分支A。
#         （一直持续这个循环直到Products中的所有对象都操作结束)
#
#         操作分支A：
#         在对应的shop数据中找到对应的外键merchant，并在Merchant表格中找到对应的merchant数据
#         现在利用这些已有的数据customer,shop,merchant, address_line和sale_time创建一个order(其中的total_price设置=0),并获取其order id
#         然后将order id与对应的shop id都存入temp中创建一个对应的{shopId,OrderId}数据
#         然后利用已创建的order以及前面获取的product, price与quantity 在OrderItem中创建orderitem数据
#
#         操作分支B：
#         若当前的Products中的新的对象{productId, quantity}找到的对应的Shop表格中对应的shop的数据shop id在temp中找到对应的shopId数据，
#         则先使用ProductId在Product表格中找到对应的product数据，获取其price
#         然后在OrderItem表格中创建新数据:使用OrderId(来自对应的temp中的对象的数据)，product，price 和 {productId, quantity}中的quantity

            # 创建订单与订单项
            with transaction.atomic():
                temp = []
                for product_data in products_data:
                    product_id = product_data['product_id']
                    quantity = int(product_data['quantity'])

                    # 获取产品信息及其关联的店铺
                    product = Product.objects.get(id=product_id)
                    shop = product.shop

                    # 检查是否已有该商店的订单
                    order = None
                    for item in temp:
                        if item['shopId'] == shop.id:
                            order = Order.objects.get(id=item['orderId'])
                            break

                    if not order: # 没有找到订单，创建新的订单
                        merchant = shop.merchant
                        order = Order(
                            customer=customer,
                            merchant=merchant,
                            shop=shop,
                            total_price=0,
                            sale_time=sale_time,
                            address_line=address_line
                        )
                        order.save()  # 确保Order对象被保存并分配了主键
                        print("Order ID after save:", order.pk)  # 调试输出，确认ID已分配

                        temp.append({'shopId': shop.id, 'orderId': order.id})

                    # 接下来创建OrderItem实例
                    OrderItem.objects.create(
                        order=order,
                        product=product,
                        product_price=product.price,
                        quantity=quantity
                    )
                transaction.commit()

            # TODO:此处再添加一部分功能，要求等保存结束后计算每个order的total_price的值（还未实现，看model.py中的代码能否自动更新）
            context = {
                'orders': temp,
                'total_price': total_price
            }
            return render(request, "payment.html", context)
        except Customer.DoesNotExist:
            print("Customer does not exist")
            return JsonResponse({'message': 'Customer does not exist'}, status=404)
        except Shop.DoesNotExist:
            print("Customer does not exist")
            return JsonResponse({'message': 'Shop does not exist'}, status=404)
        except Product.DoesNotExist:
            print("Product does not exist")
            return JsonResponse({'message': 'Product does not exist'}, status=404)
        except Exception as e:
            transaction.rollback()
            print(e)
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)


# # TODO: 接收前端传来的cart info，然后将这些数据在Order表格与OrderItem中创建对应的数据，然后返回order_id
# def generate_payment(request):
#     if request.method == 'POST':
#         username = request.session.get('username', None)  # customer username
#         if username is None:
#             return JsonResponse({'message': 'Unauthorized access'}, status=401)
#
#         user_type = request.session.get('user_type', None)
#         if not username or user_type != '1':
#             return JsonResponse({'error': 'Error user type or not logged in'}, status=400)
#
#         # TODO: 通过username在Customer中获取对应的customer数据
#         # TODO: 接收传来的数据中的products与total_price, address_id
#         # TODO: 通过address_id在Address表格中获取address_line的值，并存储为变量
#         # TODO: 获取现在的时间记录为sale_time，存储为变量
#         '''
#         TODO:
#         现在先创建一个List，其中存储的数据类型为{shopId,OrderId}，设这个List叫temp
#         现在在Products中有多个对象{productId, quantity}，以一个对象为例：
#         先使用对象中productId的在Product表格中寻找对应的product数据，获取其对应的price与外键shop
#         利用外键shop在Shop表格找到对应的数据shop然后获取其shop id
#         如果现在操作的这个数据获取到的shopId，遍历temp中的所有数据，如果找到有与之对应的shopId，则进行下面的操作分支B。若没有找到，则进行下面的操作分支A。
#         （一直持续这个循环直到Products中的所有对象都操作结束)
#
#         操作分支A：
#         在对应的shop数据中找到对应的外键merchant，并在Merchant表格中找到对应的merchant数据
#         现在利用这些已有的数据customer,shop,merchant, address_line和sale_time创建一个order(其中的total_price设置=0),并获取其order id
#         然后将order id与对应的shop id都存入temp中创建一个对应的{shopId,OrderId}数据
#         然后利用已创建的order以及前面获取的product, price与quantity 在OrderItem中创建orderitem数据
#
#         操作分支B：
#         若当前的Products中的新的对象{productId, quantity}找到的对应的Shop表格中对应的shop的数据shop id在temp中找到对应的shopId数据，
#         则先使用ProductId在Product表格中找到对应的product数据，获取其price
#         然后在OrderItem表格中创建新数据:使用OrderId(来自对应的temp中的对象的数据)，product，price 和 {productId, quantity}中的quantity
#         '''
#
#         # TODO:操作结束则保存Order与OrderItem表格，注意错误处理
#         context = {
#             'orders': temp,
#             'total_price': total_price
#         }
#         return render(request, "payment.html", context)
#
#     return JsonResponse({'error': 'Invalid request'}, status=400)
