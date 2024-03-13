from django.shortcuts import render


# Create your views here.
def main_page(request):
    print("redirect to my cart page")
    return render(request, 'cart.html')


