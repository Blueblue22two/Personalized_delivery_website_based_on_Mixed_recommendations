from django.shortcuts import render


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


# upload
def upload_cart(request):
    if request.method == 'POST':
        # TODO: 接收前端传来的关于cart的改变，将改变存入CartItem表格中
        return
    return
