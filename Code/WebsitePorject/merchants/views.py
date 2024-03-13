from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.http import JsonResponse
from accounts.models import Merchant, Shop


# Create your views here.

# -- My store --
def my_store(request):
    username = request.session.get('username')
    user_type = request.session.get('user_type')
    print("user_type: ", user_type)

    if user_type != '2':  # if user type != merchant
        print("Error: Non merchant user type!")
        logout_view(request)

    try:
        # TODO: 返回store的数据
        merchant = Merchant.objects.get(username=username)
        shop = merchant.shop
        return render(request, 'my_store.html', {'shop': shop})
    except Merchant.DoesNotExist:
        return render(request, 'Create_store.html')


# --# logout(clear session) & redirect to main page--
def logout_view(request):
    print("log out...")
    logout(request)
    print("log out successfully")
    return HttpResponseRedirect('/')


# register a new store for a new merchant
def new_store(request):
    if request.method == 'POST':
        # TODO: 接受前端传来的数据，以及session中的username
        username = request.session.get('username')
        user_type = request.session.get('user_type')


        # TODO: 将数据存储到对应的Shop表格中，并更新对应的Merchant表格的数据的shop = models.ForeignKey

        # TODO: 返回创建成功信息，并在response中附上重定向url='/merchants/my_store/'

        return
    # if request != post, return error
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


def manage(request):
    return
