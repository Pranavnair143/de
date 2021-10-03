from rest_framework import pagination, viewsets

from .serializers import ProductSerializer,ProductPagination
from .models import Product

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all().order_by('id')
    serializer_class=ProductSerializer
    pagination=ProductPagination