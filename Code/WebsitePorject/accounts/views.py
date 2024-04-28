from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth import login, logout
from accounts.models import Customer, Merchant
from django.contrib.auth.hashers import make_password, check_password


# -- logout(clear session) & redirect to main page--
def logout_view(request):
    logout(request) # logout and clear session
    print("log out successfully,redirect to /")
    return HttpResponseRedirect('/')


# -- Checks whether the user is logged in from the session, if not then logout--
def get_user_info(request):
    print("get user info...")
    username = request.session.get('username', None)
    user_type = request.session.get('user_type', None)  # if not exist then return none

    if username and user_type:
        data = {
            'is_logged_in': True,
            'username': username,
            'user_type': user_type
        }
        print("get user info successfully")
        return JsonResponse(data,status=200)
    else:
        print("get user info failed, not login")
        return logout_view(request)


# -- Checks whether the user is logged in from the session--
def get_info(request):
    print("get info...")
    username = request.session.get('username', None)
    user_type = request.session.get('user_type', None)  # if not exist then return none

    if username and user_type:
        data = {
            'is_logged_in': True,
            'username': username,
            'user_type': user_type
        }
        print("get info successfully")
        return JsonResponse(data, status=200)
    else:
        data = {'is_logged_in': False}
        print("get info failed, not login")
        return JsonResponse(data, status=403)


# -- Log In --
def login_customer(request):
    if request.method == 'POST':
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


# This Function to receive form and login account for user
def submit_log(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_type = request.POST.get('userType')
        print("Username:", username)
        print("Password:", password)
        print("User Type:", user_type)

        # if user_type != '1' and user_type != '2':
        if user_type != '1' and user_type != '2':
            print("error: Non-existent user type: " + user_type)
            return JsonResponse({'message': 'error: Non-existent user type.'}, status=400)

        try:
            if user_type == '1':  # customer
                customer = Customer.objects.get(username=username)
                hash_password = customer.password
                if not check_password(password, hash_password):  # validate password
                    return JsonResponse({'message': 'Invalid password.'}, status=401)
            else:  # merchant
                merchant = Merchant.objects.get(username=username)
                hash_password = merchant.password
                if not check_password(password, hash_password):  # validate password
                    return JsonResponse({'message': 'Invalid password.'}, status=401)

        except Customer.DoesNotExist:
            return JsonResponse({'error': 'Merchant: username does not exist.'}, status=404)
        except Merchant.DoesNotExist:
            return JsonResponse({'error': 'Merchant: username does not exist.'}, status=404)

        redirect_url = '/accounts/main/'
        response = JsonResponse({'message': username + ' login successfully.', 'redirect_url': redirect_url},
                                status=200)
        # session
        request.session['username'] = username
        request.session['user_type'] = user_type
        return response

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


# This Function to receive form and register an account for user
def submit_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        user_type = request.POST.get('userType')
        print("Username:", username)
        print("Password:", password)
        print("Phone:", phone)
        print("User Type:", user_type)

        # hash password
        hash_password = make_password(password)
        print("Hash Password:", hash_password)

        # if user_type != '1' and user_type != '2':
        if user_type != '1' and user_type != '2':
            print("Error: Non-existent user type: " + user_type)
            return JsonResponse({'message': 'Error: Non-existent user type.'}, status=400)

        try:
            if user_type == '1': # customer
                if check_duplication_customer(username):
                    customer_info = Customer()
                    customer_info.username = username
                    customer_info.password = hash_password
                    customer_info.phone_number = phone
                    # Store info into the database
                    customer_info.save()
                else:
                    return JsonResponse({'message': 'Error: Already have a same username.'}, status=409)
            else: # merchant
                if check_duplication_merchant(username):
                    merchant_info = Merchant()
                    merchant_info.username = username
                    merchant_info.password = hash_password
                    merchant_info.phone_number = phone
                    # Store info into the database
                    merchant_info.save()
                else:
                    return JsonResponse({'message': 'Error: Already have a same username.'}, status=409)
        except Exception as e:
            print("Error connecting to database:", str(e))
            return JsonResponse({'error': 'Error connecting to database.'}, status=500)

        # Response
        redirect_url = '/accounts/main/'
        response = JsonResponse({'message': username + ' saved successfully.', 'redirect_url': redirect_url},
                                status=200)

        # Session
        request.session['username'] = username
        request.session['user_type'] = user_type
        return response

    return JsonResponse({'error': 'Invalid request method.'}, status=400)


# This function is used to check if the customer username is duplicated
def check_duplication_customer(name):
    existing_customer = Customer.objects.filter(username=name).first()
    if existing_customer:
        print("Already have a same username!")
        return False
    return True


# This function is used to check if the merchant username is duplicated
def check_duplication_merchant(name):
    existing_merchant = Merchant.objects.filter(username=name).first()
    if existing_merchant:
        print("Already have a same username!")
        return False
    return True


# Function jump to main page
def main_page(request):
    print("redirect to main page")
    return render(request, 'main_index.html')


def search(request):
    return render(request, 'search.html')
