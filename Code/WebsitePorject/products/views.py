import json

from django.forms import model_to_dict
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from customers.models import Comment
from merchants.models import Product
from django.db.models import Avg, Count
from django.core import serializers

# Create your views here.


# display product page
def product_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    shop_name = product.shop.name
    average_rating = Comment.objects.filter(product=product).aggregate(Avg('rating'))['rating__avg'] or 'Not Rated'
    if average_rating != 'Not Rated':
        average_rating = round(average_rating, 1)
    else:
        average_rating=0
    # return data
    context = {
        'shop_name':shop_name,
        'product': product,
        'average_rating': average_rating,
    }
    return render(request, 'product.html', context)


def get_comment(request):
    if request.method == 'POST':
        product_id = request.POST.get('productId')
        print(f"get comment function > product id: {product_id}")

        comments = Comment.objects.filter(product_id=product_id).select_related('customer')
        comments_data = []

        for comment in comments:
            comment_dict = model_to_dict(comment, fields=['text', 'rating'])
            comment_dict['customer_username'] = comment.customer.username
            comments_data.append(comment_dict)

        return JsonResponse({'comments': comments_data}, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)


# function of category and category page
def product_category(request,category_name):
    context = {
        'category_name': category_name,
    }
    return render(request,'category.html',context)


def category_info(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        category_name = data.get('category_name')
        print(f"category_info function, category: {category_name}")

        products_data = Product.objects.filter(category=category_name).annotate(
            product_rate_number=Count('comments')
        ).values(
            'id', 'name', 'price', 'category', 'image_path', 'average_rate', 'product_rate_number'
        )

        products_data = list(products_data)
        print("Returning JsonResponse")
        return JsonResponse({'products': products_data}, safe=False)

    # if request != post, return error
    return JsonResponse({'error': 'Invalid request method.'}, status=400)