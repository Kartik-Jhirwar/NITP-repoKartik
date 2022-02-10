import http
from django.shortcuts import render 
from .models import Data
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request , 'index.html')

def login(request):
    return render(request , 'login.html')

def purchase(request):
    return render(request , 'purchase.html')

def register(request):
    return render(request , 'register.html')

def dashboard(request):
    return render(request , 'dashboard.html')

def search_result(request):

    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            data = Data.objects.filter(college_name__icontains=query) 
            return render(request, 'search_result.html', {'data':data})
        else:
            print("No information to show")
            return render(request, 'search_result.html', {})