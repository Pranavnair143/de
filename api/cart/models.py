from django.db import models

from api.user.models import CustomUser
from api.product.models import Product


class Cart(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,unique=False)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,unique=False)
    qnty=models.IntegerField(default=50,unique=False)

    def __str__(self) -> str:
        return self.user.name