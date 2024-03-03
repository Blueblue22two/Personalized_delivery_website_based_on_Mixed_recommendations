from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from accounts.models import Customer, Merchant


# Create your views here.

# redirect to login page of customer
def login_customer(request):
    return render(request, 'login_customer.html')


# redirect to login page of merchant
def login_merchant(request):
    return render(request, 'login_merchant.html')


# register
def customer_register(request):
    if request.method == 'POST':
        response = submit_form(request)
    else:
        return render(request, 'register_customer.html')


def merchant_register(request):
    if request.method == 'POST':
        response = submit_form(request)
    else:
        return render(request, 'register_merchant.html')


"""
This Function to receive form and register an account for user
"""


def submit_form(request):
    if request.method == 'POST':
        # 获取POST请求中的表单数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')
        phone = request.POST.get('phone')
        user_type = request.POST.get('user_type')

        # TODO 打印数据
        print("Username:", username)
        print("Password:", password)
        print("Confirm Password:", confirm_password)
        print("Phone:", phone)
        print("User Type:", user_type)

        # TODO 检查用户类型
        if user_type != 1 and user_type != 2:  # customer
            print("Error: Non-existent user type.")
            return JsonResponse({'message': 'Error: Non-existent user type.'})

        # TODO Connect the database
        if user_type == 1:
            customer_info = Customer()
            customer_info.username = username
            customer_info.password = password
            customer_info.phone_number = phone
            # TODO Check whether there are duplicate user names in database
            existing_customer = Customer.objects.filter(username=username).first()
            if existing_customer:
                print("Already have a same username!")
                return
            # TODO Store info into the database
            customer_info.save()

        # TODO Check whether there are duplicate user names in database

        # TODO Store info into the database

        # TODO create a session
        # 响应成功消息
        return JsonResponse({'message': + username + ' saved successfully.'})

    # 如果请求不是POST，返回错误消息
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


"""
This function is used to check if the username is duplicated
"""
def check_duplication(name):
    existing_customer = Customer.objects.filter(username=name).first()
    if existing_customer:
        print("Already have a same username!")
        # TODO error information
        return False


"""
Function jump to main page
"""


def main(request):
    # TODO：若用户登录、注册成功，根据用户类型返回界面
    return render(request, 'main.html')
