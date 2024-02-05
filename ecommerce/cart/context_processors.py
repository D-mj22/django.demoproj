from cart.models import Cart

def total_count(request):               # total items in cart symbol navbar
    u=request.user
    item_count=0
    try:
        c=Cart.objects.filter(user=u)
        for i in c:
            item_count+=i.quantity
    except:
        item_count=0
    return {'count':item_count}



