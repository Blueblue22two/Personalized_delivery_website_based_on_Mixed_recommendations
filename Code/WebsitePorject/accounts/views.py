from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from accounts.models import Customer, Merchant


# Create your views here.


# -- Log In --
def login_customer(request):
    if request.method == 'POST':
        # TODO: receive
        print("> Post: request of a customer login ")
        response = submit_log(request)
        return response
    else:
        return render(request, 'login_customer.html')


def login_merchant(request):
    if request.method == 'POST':
        print("> Post: request of a merchant login")
        response = submit_log(request)
        return response
    else:
        return render(request, 'login_merchant.html')


"""
This Function to receive form and login account for user
"""
def submit_log(request):
    if request.method == 'POST':
        # get the form data
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_type = request.POST.get('userType')

        print("Username:", username)
        print("Password:", password)
        print("User Type:", user_type)

        # if user_type != '1' and user_type != '2':  # 注意：比较的是字符串
        if user_type != '1' and user_type != '2':  # customer
            print("Error: Non-existent user type: " + user_type)
            return JsonResponse({'message': 'Error: Non-existent user type.'}, status=400)

        # Connect the database
        try:
            if user_type == '1':  # customer
                if Customer.objects.filter(username=username, password=password).exists():
                    # User exists and password is correct
                    pass  # You can perform additional actions if needed
                else:
                    # User does not exist or password is incorrect
                    return JsonResponse({'message': 'Invalid username or password.'}, status=400)

            else:  # merchant
                if Merchant.objects.filter(username=username, password=password).exists():
                    # User exists and password is correct
                    pass  # You can perform additional actions if needed
                else:
                    # User does not exist or password is incorrect
                    return JsonResponse({'message': 'Invalid username or password.'}, status=400)
        except Exception as e:
            print("Error connecting to database:", str(e))
            return JsonResponse({'error': 'Error connecting to database.'}, status=500)

        # Create a response
        redirect_url = '/accounts/main/'
        response = JsonResponse({'message': username + ' login successfully.', 'redirect_url': redirect_url},
                                status=200)
        # TODO:cookie更换为session
        # create a cookie
        response.set_cookie('user_type', user_type, max_age=3600)  # Cookie will last for 1 hour
        response.set_cookie('username', username, max_age=3600)
        return response

    # if request != post, return error
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


# -- Register --
def customer_register(request):
    if request.method == 'POST':
        print("> Post: request of new customer")
        response = submit_register(request)
        return response
    else:
        return render(request, 'register_customer.html')


def merchant_register(request):
    if request.method == 'POST':
        print("> Post: request of new merchant")
        response = submit_register(request)
        return response
    else:
        return render(request, 'register_merchant.html')


"""
This Function to receive form and register an account for user
"""
def submit_register(request):
    if request.method == 'POST':
        # get the form data
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        user_type = request.POST.get('userType')

        print("Username:", username)
        print("Password:", password)
        print("Phone:", phone)
        print("User Type:", user_type)

        # if user_type != '1' and user_type != '2':  # 注意：比较的是字符串
        if user_type != '1' and user_type != '2':  # customer
            print("Error: Non-existent user type: " + user_type)
            return JsonResponse({'message': 'Error: Non-existent user type.'}, status=400)

        # Connect the database
        try:
            if user_type == '1':
                if check_duplication_customer(username):
                    customer_info = Customer()
                    customer_info.username = username
                    customer_info.password = password
                    customer_info.phone_number = phone
                    # Store info into the database
                    customer_info.save()
                else:
                    return JsonResponse({'message': 'Error:Already have a same username.'})
            else:
                if check_duplication_merchant(username):
                    merchant_info = Merchant()
                    merchant_info.username = username
                    merchant_info.password = password
                    merchant_info.phone_number = phone
                    # Store info into the database
                    merchant_info.save()
                else:
                    return JsonResponse({'message': 'Error:Already have a same username.'})
        except Exception as e:
            print("Error connecting to database:", str(e))
            return JsonResponse({'error': 'Error connecting to database.'}, status=500)

        # Create a response
        redirect_url = '/accounts/main/'
        response = JsonResponse({'message': username + ' saved successfully.', 'redirect_url': redirect_url},
                                status=200)
        # TODO:cookie更换为session
        # create a cookie
        response.set_cookie('user_type', user_type, max_age=3600)  # Cookie will last for 1 hour
        response.set_cookie('username', username, max_age=3600)

        return response

    # if request != post, return error
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


"""
This function is used to check if the customer username is duplicated
"""
def check_duplication_customer(name):
    existing_customer = Customer.objects.filter(username=name).first()
    if existing_customer:
        print("Already have a same username!")
        return False
    return True


"""
This function is used to check if the merchant username is duplicated
"""
def check_duplication_merchant(name):
    existing_merchant = Merchant.objects.filter(username=name).first()
    if existing_merchant:
        print("Already have a same username!")
        return False
    return True


"""
Function jump to main page
"""
def main_page(request):
    print("redirect to main page")
    return render(request, 'main.html')
