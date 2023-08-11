from rest_framework import serializers

from .models import (   
    partQty,   
)
class partQtySerializer(serializers.ModelSerializer):
     class Meta:
        model = partQty
        fields = '__all__'