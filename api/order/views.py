from django.utils import translation
from rest_framework import viewsets
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

from .serializer import OrderSerializer
from .models import Order, OrderSummary
from api.cart.models import Cart

def validate_user_session(id,token):
    UserModel=get_user_model()
    try:
        user=UserModel.objects.get(pk=id)
        if user.session_token==token:
            return True
        return False
    except UserModel.DoesNotExist:
        return False

@csrf_exempt
def add(request,id,token):
    if not validate_user_session(id,token):
        return JsonResponse({'message':'Please re-login','code':'1','success':False})
    UserModel=get_user_model()
    try:
        user=UserModel.objects.get(pk=id)
    except UserModel.DoesNotExist:
        return JsonResponse({'message':'User does not exist','success':False})
    cart=Cart.objects.filter(user=user)
    total=0
    for i in cart:
        total+=i.product.price*i.qnty
    if request.method=='POST':
        state=request.POST.get('state','None')
        district=request.POST.get('district',"None")
        city=request.POST.get('city','None')
        address=request.POST.get('address',"None")
        order=Order(user=user,total=total,state=state,district=district,city=city,address=address)
        order.save()
        orderSummaryList=[]
        for i in cart:
            orderSummary=OrderSummary(order=order,product=i.product,qnty=i.qnty,user=user)
            orderSummary.save()
            orderSummaryList.append(orderSummary)
        orderSummaryList=[i for i in OrderSummary.objects.filter(order=order).values()]
        cart.delete()
        return JsonResponse({'success':True,'message':'Order placed successfully','orderSummary':orderSummaryList})

@csrf_exempt
def show_orders(self,id,token):
    if not validate_user_session(id,token):
        return JsonResponse({'message':'Please re-login','code':'1','success':False})
    UserModel=get_user_model()
    try:
        user=UserModel.objects.get(pk=id)
    except UserModel.DoesNotExist:
        return JsonResponse({'message':'User does not exist','success':False})
    ordersItems=[j for j in OrderSummary.objects.filter(user=user).values()]
    return JsonResponse({"success":True,"Orders":ordersItems})