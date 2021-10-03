from rest_framework import viewsets
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

from .serializers import CartSerializer
from .models import Cart
from api.product.models import Product

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
def add(request,id,token,product_id):
    if not validate_user_session(id,token):
        return JsonResponse({'message':'Please re-login','success':False})
    UserModel=get_user_model()
    try:
        user=UserModel.objects.get(pk=id)
    except UserModel.DoesNotExist:
        return JsonResponse({'message':'User does not exist','success':False})
    if request.method=='POST':
        qnty=request.POST.get('qnty', 1);
        product=Product.objects.get(id=2)
        prev=Cart.objects.filter(user=user,product=product).exists()
        if prev:
            cartExists=Cart.objects.get(user=user,product=product_id)
            cartExists.qnty+=qnty
            cartExists.save()
        else:
            cart=Cart(user=user,qnty=qnty,product=product)
            cart.save()
        return JsonResponse({'success':True,'message':'Added to cart successfully'})

class CartViewSet(viewsets.ModelViewSet):
    serializer_class=CartSerializer

    def get_queryset(self):
        UserModal=get_user_model()
        id=self.kwargs['id']
        token=self.kwargs['token']
        if not validate_user_session(id,token):
            return JsonResponse({'message':'Please re-login','success':False})
        return Cart.objects.filter(user=UserModal.objects.get(id=id)).values()

@csrf_exempt
def showCart(request,id,token):
    if not validate_user_session(id,token):
        return JsonResponse({'message':'Please re-login','success':False})
    UserModel=get_user_model()
    try:
        user=UserModel.objects.get(pk=id)
    except UserModel.DoesNotExist:
        return JsonResponse({'message':'User does not exist','success':False})
    cartItems=[i for i in Cart.objects.filter(user=user).values()]
    return JsonResponse({"success":True,"cartItems":cartItems})