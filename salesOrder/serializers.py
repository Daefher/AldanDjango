from rest_framework import serializers
from .models import (
   salesOrder,
   salesOrderDtl,
   paymentData
   )


class salesOrderSerializer(serializers.ModelSerializer):     
     class Meta:
        model = salesOrder
        fields = '__all__'

class salesOrderDtlSerializer(serializers.ModelSerializer):
    class Meta:
      model = salesOrderDtl
      fields = '__all__'

class salesOrderAndDtlSerializer(serializers.ModelSerializer):
     salesOrderDtl = salesOrderDtlSerializer(many=True, read_only=True)     
     class Meta:
        model = salesOrder
        fields = '__all__'