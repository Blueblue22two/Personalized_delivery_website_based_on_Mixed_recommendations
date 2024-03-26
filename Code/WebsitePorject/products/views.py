from django.forms import model_to_dict
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from customers.models import Comment
from merchants.models import Product
from django.db.models import Avg
from django.core import serializers

# Create your views here.


# display product page
def product_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    average_rating = Comment.objects.filter(product=product).aggregate(Avg('rating'))['rating__avg'] or 'Not Rated'
    if average_rating != 'Not Rated':
        average_rating = round(average_rating, 1)
    else:
        average_rating=0
    # return data
    context = {
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
            # 直接访问外键关联的Customer对象获取username
            comment_dict['customer_username'] = comment.customer.username
            comments_data.append(comment_dict)

        return JsonResponse({'comments': comments_data}, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)