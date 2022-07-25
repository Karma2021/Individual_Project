from product.models import Product
from django.contrib.auth.decorators import login_required


from multiprocessing import context
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from product.models import Product
from django.contrib.auth.decorators import login_required
from product.models import Product
from django.contrib.auth.decorators import login_required


from multiprocessing import context
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import redirect, render
from cart.cart import Cart
from orders.models import Order

from cart.cart import Cart
# Create your views here.



def book(request):
    product=Product.objects.all().order_by('-id')
    return render (request,'books.html',{'products':product,'nbar': 'watch'})





# def product(request,id):
#     data=Product.objects.get(id=id)
#     print(id)
#     return render(request,"product.html",{'data':data})

 

def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("/product")


def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


def cart_detail(request):
    return render(request, 'cart.html')



def checkout(request):
    if request.method=="POST":
        phonenumber=request.POST.get('phonenumber')
        email=request.POST.get('email')
        address=request.POST.get('address')
        pincode=request.POST.get('pincode')
        payment=request.POST.get('payment')
        cart=request.session.get('cart')
        uid=request.session.get('_auth_user_id')
        user=User.objects.get(pk=uid)
        
        for i in cart:
            a=(float(cart[i]['price']))
            b=cart[i]['quantity']
            total=a*b
            
            order=Order(
                user=user,
                name=cart[i]['name'],
                price=cart[i]['price'],
                quantity=cart[i]['quantity'],
                image=cart[i]['image'],
                phonenumber=phonenumber,
                email=email,
                address=address,
                pincode=pincode,
                payment=payment,
                total=total,
            )
            order.save()
        request.session['cart']={}
        return redirect("/")
        

def order(request):
    uid=request.session.get('_auth_user_id')
    user=User.objects.get(pk=uid)
    order=Order.objects.filter(user=user)
    return render(request, "order.html",{'order':order})