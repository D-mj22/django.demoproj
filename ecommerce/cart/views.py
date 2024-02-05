from django.shortcuts import render
from shop.models import Product
from cart.models import Cart, Order, Account
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
@login_required
def cartview(request):                  # view cart products of current/one user
    total = 0
    u=request.user
    try:
        list1=Cart.objects.filter(user=u)
        for i in list1:
            total+=i.quantity * i.product.price
    except:
        pass
    return render(request,'cartview.html',{'l':list1,'tot':total})

@login_required
def addtocart(request,p):
    item=Product.objects.get(name=p)    # get details of referenced product from product table
    u=request.user                   # get details of current user logged in
    try:
        cart=Cart.objects.get(user=u,product=item)  # for one user only one record with a particular record should be there in Cart table; so we use get()
        if(cart.product.stock > 0):       # check if stock is available before quantity is incremented
            cart.quantity+=1
            cart.save()
            item.stock -= 1
            item.save()
    except:
        if(item.stock>0):                           # check if stock is there to add.
            cart=Cart.objects.create(product=item,user=u,quantity=1)
            # cart.product.stock-=1
            cart.save()
            item.stock-=1
            item.save()
    return cartview(request)

@login_required
def decrementcart(request,p):
    item=Product.objects.get(name=p)
    u=request.user
    try:
        cart=Cart.objects.get(user=u,product=item)
        if(cart.quantity>1):                # if quantity=1 then, product should be deleted from cart
            cart.quantity-=1
            cart.save()
            item.stock += 1
            item.save()
        else:
            cart.delete()
            item.stock += 1
            item.save()
    except:
        pass
    return cartview(request)

@login_required
def delete_cart(request,p):
    item=Product.objects.get(name=p)
    u=request.user
    try:
        cart=Cart.objects.get(user=u,product=item)
        cart.delete()
        item.stock+=cart.quantity
        item.save()
    except:
        pass

    return cartview(request)

@login_required
def orderform(request):
    u=request.user
    if request.method=="POST":
        a=request.POST['a']
        p=request.POST['p']
        n=request.POST['n']
        cart=Cart.objects.filter(user=u)
        total=0
        for i in cart:                      # Total Bill amount of user
            total += i.quantity * i.product.price
        #return HttpResponse(total)
        try:
            a_num=Account.objects.get(acctnum=n)        # to retrieve details of given acctnum for payment
            if a_num:
                if a_num.amount > total:
                    a_num.amount=a_num.amount - total
                    a_num.save()
                    # return HttpResponse("Payment deducted")
                    for i in cart:          # to add all records in this user's cart to order table after payment
                        o=Order.objects.create(user=u,product=i.product,address=a,phone=p,no_of_items=i.quantity,order_status="paid")
                        o.save()
                    cart.delete()           # to delete cart records of this user after he ordered.
                    msg="Your order has been placed successfully"
                    return render(request,'orderdetail.html',{'msg':msg})
                else:
                    msg="Insufficient balance. Your order cannot be processed"
                    return render(request, 'orderdetail.html', {'msg': msg})
        except:
            pass

    return render(request,'orderform.html')

@login_required()
def orderview(request):
    u=request.user
    msg="Here is the list of your orders"
    o=Order.objects.filter(user=u)
    return render(request,'orderdetail.html',{'msg':msg,'order':o,'u':u})
