from rest_framework import serializers

from .models import Order,OrderSummary



class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Order
        fields='__all__'


class OrderSummarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=OrderSummary
        fields='__all__'