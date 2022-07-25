from django.shortcuts import render, redirect
from product.models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    product=Product.objects.all().order_by('-id')[0:3]
    dis=Product.objects.all().order_by('-id')[0:1]
    print(product)
    return render(request,'index.html', {'product':product,'dis':dis})
    
def about(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact.html')

