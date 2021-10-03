from rest_framework import serializers
from .models import Product,ProductReview
from rest_framework.pagination import PageNumberPagination

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

class ProductReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=ProductReview
        fields='__all__'

class ProductPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000