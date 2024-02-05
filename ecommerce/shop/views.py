from django.shortcuts import render,redirect
from shop.models import Category,Product
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse

# Create your views here.
def allcategories(request):
    a=Category.objects.all()
    return render(request,'category.html',{'a':a})

# Function to view product details from category page.
def view(request,p):
    b=Category.objects.get(name=p)
    c=Product.objects.filter(category=b)
    return render(request,'products.html',{'b':b,'c':c})

def product_detail(request,p):
    d=Product.objects.get(name=p)
    return render(request,'details.html',{'d':d})

def register(request):
    if(request.method=='POST'):
        u=request.POST['u']
        p1 = request.POST['p1']
        p2 = request.POST['p2']
        e = request.POST['e']
        f = request.POST['f']
        l = request.POST['l']
        if(p1==p2):
            user=User.objects.create_user(username=u,password=p1,first_name=f,last_name=l,email=e)
            user.save()
            return redirect('shop:allcat')
        else:
            return HttpResponse("Passwords do not match")
    return render(request,'register.html')

def user_login(request):
    if(request.method=='POST'):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('shop:allcat')
        else:
            return HttpResponse("Invalid login details")
    return render(request,'login.html')

@login_required
def user_logout(request):
    logout(request)
    return render(request,'login.html')

