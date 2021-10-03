from rest_framework import routers
from django.urls import path,include

from . import views

#router=routers.DefaultRouter()
#router.register(r'',views.CartViewSet, basename='Cart')

urlpatterns=[
    path('<str:id>/<str:token>',views.showCart,name="cart_show"),
    path('add/<str:id>/<str:token>/<int:product_id>',views.add,name='cart_add'),
]