from django.db import models
from api.category.models import Category
from api.user.models import CustomUser


class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True,null=True)
    name=models.CharField(max_length=250,default='ds')
    brand_name=models.CharField(max_length=250,default='ds')
    type=models.CharField(max_length=250,default='ds')
    description=models.CharField(max_length=450,default='ds')
    price=models.FloatField(default=0)
    stock=models.IntegerField(default=50)
    is_active=models.BooleanField(default=True,blank=True)
    imageUrl=models.CharField(max_length=500,default='ds')

    def __str__(self):
        return self.name



class ProductReview(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    rate=models.IntegerField(default=0)
    review=models.TextField(default='ds')

    def __str__(self) -> str:
        return self.rate+"  ("+self.review+")"