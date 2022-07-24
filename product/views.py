from product.models import Product
from django.contrib.auth.decorators import login_required


from multiprocessing import context
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


# Create your views here.



def book(request):
    product=Product.objects.all().order_by('-id')
    return render (request,'books.html',{'products':product,'nbar': 'watch'})