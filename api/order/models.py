from django.db import models
from api.user.models import CustomUser
from api.product.models import Product


class Order(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    address=models.CharField(max_length=700,default='ds')
    city=models.CharField(max_length=60,default='ds')
    district=models.CharField(max_length=60,default='ds')
    state=models.CharField(max_length=60,default='ds')
    total=models.FloatField(default=0)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.name+"  "+str(self.created_at)
    
class OrderSummary(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    qnty=models.IntegerField(default=0)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,default=2)
    def __str__(self) -> str:
        return self.user.name+"  "+str(self.product.name)
    

