from django.shortcuts import get_object_or_404, render
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import partQtySerializer
from .models import partQty
from company.models import company
from .permissions import CompanyOwnerEditCancel
#from part.permission import AuthorEditCancel

# Create your views here.


class getPartQtys(
        generics.RetrieveAPIView):
    serializer_class = partQtySerializer
    queryset = partQty.objects.all()


class getPartQtyByPartid(
        generics.RetrieveAPIView):
    serializer_class = partQtySerializer
    lookup_field = ('companyId', 'partId')
    queryset = partQty.objects.all()
    permission_classes = (CompanyOwnerEditCancel,)

    def get_object(self):
        obj = get_object_or_404(self.queryset, companyId=self.request.data.get(
            'companyId'), partId=self.request.data.get('partId'))
        self.check_object_permissions(self.request, obj)
        return obj


class getPartQtyById(
        generics.RetrieveAPIView):
    serializer_class = partQtySerializer
    queryset = partQty.objects.all()
    permission_classes = (CompanyOwnerEditCancel,)


class insertPartQty(
        generics.CreateAPIView):
    serializer_class = partQtySerializer
    queryset = partQty.objects.all()
    permission_classes = (CompanyOwnerEditCancel, )


class updatePartQty(
        generics.UpdateAPIView):
    serializer_class = partQtySerializer
    queryset = partQty.objects.all()
    permission_classes = (CompanyOwnerEditCancel,)
    

