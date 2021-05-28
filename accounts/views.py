from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(req):
    return render(req,'accounts/dashboard.html')

def products(req):
    return HttpResponse('products page')

def customers(req):
    return HttpResponse('customers page')


'''
django searches in this pattern
    -->accounts
        -->templates
            -->accounts
                dashboard.html
                products.html
                customers.html
'''
