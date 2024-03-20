from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from customers.models import Comment
from merchants.models import Product
from django.core import serializers

# Create your views here.


# display product page
def product_view(request, product_id):
    # 根据传入的 product id 获取特定商品
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product.html', {'product': product})


# get all the comment
def get_comment(request):
    if request.method == 'POST':
        # 从POST请求中获取productId
        product_id = request.POST.get('productId')
        # 查询相关评论
        comments = Comment.objects.filter(product_id=product_id).select_related('customer')
        # 序列化评论数据
        comments_data = serializers.serialize('json', comments)
        # 返回JSON响应
        return JsonResponse({'comments': comments_data}, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)