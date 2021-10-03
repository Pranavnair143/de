from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt

import braintree

gateway = braintree.BraintreeGateway(
  braintree.Configuration(
    environment=braintree.Environment.Sandbox,
    merchant_id='5yzrb6k6b4wvn67t',
    public_key='7j6gtf5tjrns4467',
    private_key='32de74ff074768bcb5465f7a6c73f62e'
  )
)

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
def generate_token(request,id,token):
    if not validate_user_session(id,token):
        return JsonResponse({'error':'Invalid session, Please login again.'})
    return JsonResponse({'clientToken':gateway.client_token.generate(),'success':True})

@csrf_exempt
def process_payment(request,id,token):
    if not validate_user_session(id,token):
        return JsonResponse({'error':'Invalid session, Please login again.'})
    nonce_from_client=request.POST["paymentMethodNonce"]
    amount_from_the_client=request.POST["amount"]

    result=gateway.transaction.sale({
        "amount":amount_from_the_client,
        "payment_method_nonce":nonce_from_client,
        "options":{
            "submit_for_settlement":True
        }
    })

    if result.is_success:
        return JsonResponse({
            "success":result.is_success,
            "transaction":{
                "id":result.transaction.id,
                "amount":result.transaction.amount,
                }
            })
    else:
        return JsonResponse({"error":True,"success":False})
