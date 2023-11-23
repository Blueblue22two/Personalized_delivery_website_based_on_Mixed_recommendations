from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# return the template of index page
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Hello, world. You're at the polls index.")

# redirect to login page of customer
def login_customer(request):
    return render(request,'login_customer.html')

# redirect to login page of merchant
def login_merchant(request):
    return render(request,'login_merchant.html')