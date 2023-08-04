from rest_framework import serializers
from .models import (
    part,
    partQty,
    partTran
)

class partSerializer(serializers.ModelSerializer):
     class Meta:
        model = part
        fields = '__all__'