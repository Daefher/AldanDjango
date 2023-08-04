from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from company.permissions import CompanyOwnerEditCancel
from rest_framework.generics import get_object_or_404

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

class getByHostName(
        generics.RetrieveAPIView):
    serializer_class = companySerializer
    lookup_field = 'companyWebSite'
    def get_queryset(self):
        return company.objects.filter(companyWebSite=self.kwargs['companyWebSite'])   
   
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class insertCompany(
    generics.CreateAPIView):
    serializer_class = companySerializer
    queryset = company.objects.all()
    permission_classes = (IsAuthenticated, )

class updateCompany(
    generics.UpdateAPIView):
    serializer_class = companySerializer
    queryset = company.objects.all()
    lookup_field = 'companyId'
    permission_classes = (CompanyOwnerEditCancel, )

    def get_object(self):
        obj = get_object_or_404(self.queryset, companyId=self.request.data.get('companyId'))
        self.check_object_permissions(self.request, obj)
        return obj
    
""" TODO: UPDATE THIS VIEW NOT NECESSARY AT THIS MOMENT """
class cancelCompany(
    generics.UpdateAPIView):
    serializer_class = companySerializer
    permission_classes = (CompanyOwnerEditCancel, )




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
