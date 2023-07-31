from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import (
    company,
    companyFile
    )
from .serializers import (
    companySerializer,
    companyFileSerializer
    )

# Create your views here.


class getCompany(
    generics.RetrieveAPIView):    
    serializer_class = companySerializer
    queryset = company.objects.all()
    permission_classes = (IsAuthenticated, )

class getCompanyFiles(
    mixins.ListModelMixin,
    generics.GenericAPIView):
    serializer_class = companyFileSerializer
    permission_classes = (IsAuthenticated, )
    queryset = companyFile.objects.all()
    lookup_field = 'companyId'

    def get(self, request, *args, **kwargs):
        result = self.list(request, *args, **kwargs)
        return result





