from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

# Create your views here.

# display product page
def product(request):
    # 使用get_object_or_404确保商品存在
    # product = get_object_or_404(Product, pk=product_id)
    # return render(request, 'products/product_detail.html', {'product': product})
    return