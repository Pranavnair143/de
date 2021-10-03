from rest_framework import routers
from django.urls import path,include

from . import views

urlpatterns = [
    path('<str:id>/<str:token>',views.show_orders,name='orders'),
    path('add/<str:id>/<str:token>/',views.add,name='add'),
]