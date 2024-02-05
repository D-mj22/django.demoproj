from django.shortcuts import render
from shop.models import Product
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.
def search(request):
    s=""                        #query or word searched
    word=None
    if(request.method=='POST'):
        s=request.POST['s']
        if s:
            word=Product.objects.filter(Q(name__icontains=s) | Q(desc__icontains=s))
            return render(request,'search.html',{'s':s,'word':word})
    return render(request,'category.html')