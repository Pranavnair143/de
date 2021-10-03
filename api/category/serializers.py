from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.HyperlinkedModelSerializer):#HyperlinkedModelSerializer
    class Meta:
        model=Category
        fields=['name']