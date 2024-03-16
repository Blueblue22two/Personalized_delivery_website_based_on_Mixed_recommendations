from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.conf import settings
import os


# Create your views here.


# return the template of index page
def index(request):
    # get the root directory
    root_directory = settings.BASE_DIR
    print(f"Project root directory is: {root_directory}")

    return render(request, 'main_index.html')


def login(request):
    return render(request, 'login.html')


#test
def template(request):
    return render(request, 'template.html')
