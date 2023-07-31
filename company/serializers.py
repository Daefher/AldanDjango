from rest_framework import serializers
from .models import (
    company,
    companyFile
   )

class companySerializer(serializers.ModelSerializer):
     class Meta:
        model = company
        fields = '__all__'


class companyFileSerializer(serializers.ModelSerializer):
    class Meta:
      model = companyFile
      fields = '__all__'