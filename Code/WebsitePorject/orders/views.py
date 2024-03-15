from django.shortcuts import render


# Create your views here.
def my_orders(request):
    return render(request, "my_orders.html")
