import json
import logging
from django.db.models import Sum, F
from django.utils import timezone
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, redirect
from accounts.models import Customer, Address, Shop
from cart.models import CartItem
from merchants.models import Product
from orders.models import Order, OrderItem

# get a logger named as 'django'
logger = logging.getLogger('django')


def payment_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            result = data['result']
            order_ids = data['orders']
            print(f"result: {result}")
            order_ids = [int(order_id) for order_id in order_ids.split(',') if order_id.isdigit()]
            print(order_ids)
            Order.objects.filter(id__in=order_ids).update(payment_status=result)

            redirect_url='/orders/my_orders/'
            print("Payment function done")
            return JsonResponse({'message': 'Order status updated successfully', 'redirect_url':redirect_url}, status=200)
        except Exception as e:
            print(e)
            return JsonResponse({'error': 'An error occurred during processing'}, status=500)
    else:
        return render(request, 'payment.html')


def generate_payment(request):
    if request.method == 'POST':
        try:
            logger.debug("generate_payment called")
            username = request.session.get('username', None)
            if username is None:
                logger.error("Unauthorized access attempt")
                return JsonResponse({'message': 'Unauthorized access'}, status=401)

            customer = Customer.objects.get(username=username)
            logger.debug(f"Customer retrieved: {customer.username}")

            data = json.loads(request.body)
            logger.debug(f"Request data: {data}")

            products = data.get('products', [])
            total_price = data.get('total_price', 0)
            address_id = data.get('address_id', None)
            address = Address.objects.get(id=address_id, customer=customer)
            sale_time = timezone.now()
            logger.debug(f"Address retrieved: {address.address_line}")
            logger.debug(f"Sale time: {sale_time}")

            temp = []
            with transaction.atomic():
                for product_data in products:
                    product_id = product_data.get('productId')
                    quantity = product_data.get('quantity', 1)
                    product = Product.objects.get(id=product_id)
                    shop = product.shop
                    logger.debug(f"Processing product ID {product_id} with quantity {quantity}")
                    shop_id = shop.id
                    matching_order_info = next((item for item in temp if item['shopId'] == shop_id), None)

                    if not matching_order_info:
                        merchant = shop.merchant
                        order = Order.objects.create(customer=customer, merchant=merchant, shop=shop, total_price=0,
                                                     sale_time=sale_time, address_line=address.address_line)
                        logger.debug(f"Created order ID: {order.id}")
                        temp.append({'shopId': shop_id, 'orderId': order.id})

                    else:
                        order = Order.objects.get(id=matching_order_info['orderId'])

                    # create OrderItem
                    OrderItem.objects.create(order=order, product=product, product_price=product.price, quantity=quantity)
                    # update total_price
                    calculate_order_price(order.id)

            logger.info("generate payment successfully!")
            # clear the shoppingcart
            CartItem.objects.filter(cart__customer=customer).delete()
            request.session['order_summary'] = {'orders': temp, 'total_price': total_price}
            return JsonResponse({'redirect_url': '/payment/payment_view/'}, status=200)

        except Customer.DoesNotExist:
            logger.exception("Customer not found")
            return JsonResponse({'error': 'Customer not found'}, status=404)
        except Address.DoesNotExist:
            logger.exception("Address not found")
            return JsonResponse({'error': 'Address not found'}, status=404)
        except Product.DoesNotExist:
            logger.exception("Product not found for given product ID")
            return JsonResponse({'error': 'Product not found'}, status=404)
        except Exception as e:
            logger.exception(f"Unexpected error: {str(e)}")
            return JsonResponse({'error': 'An unexpected error occurred'}, status=500)
    else:
        return JsonResponse({'message': 'error'}, status=400)


def calculate_order_price(order_id):
    try:
        with transaction.atomic():
            # get order
            order = Order.objects.get(pk=order_id)
            # calculate total_price
            total_price = OrderItem.objects.filter(order=order).aggregate(
                total=Sum(F('product_price') * F('quantity'))
            )['total'] or 0
            # update
            order.total_price = total_price
            order.save()
            print(f"Order ID: {order.id}, Total Price: {order.total_price}")
            return True
    except Order.DoesNotExist:
        print(f"Order with id {order_id} does not exist.")
        return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False


# return the order info in session
def get_order_storage(request):
    username = request.session.get('username', None)
    if username is None:
        logger.error("Unauthorized access attempt")
        return JsonResponse({'message': 'Unauthorized access'}, status=401)

    order_summary = request.session.get('order_summary', None)
    if order_summary is not None:
        # delete session data
        del request.session['order_summary']
        return JsonResponse({
            'status': 'success',
            'data': order_summary
        })
    else:
        return JsonResponse({
            'status': 'error',
            'message': 'No order data found in session.'
        })
