from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from company.permissions import CompanyOwnerEditCancel
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from .models import (
    salesOrder,
    salesOrderDtl
)
from .serializers import (
    salesOrderAndDtlSerializer,
    salesOrderSerializer,
    salesOrderDtlSerializer
)

""" GET REQUEST SALES ORDER """
class getSalesOrders(
        generics.ListAPIView):
    serializer_class = salesOrderSerializer
    lookup_field = 'companyId'
    permission_classes = (CompanyOwnerEditCancel, )

    def get_queryset(self):
        return salesOrder.objects.filter(companyId=self.kwargs['companyId'])


class getAllSalesOrder(
        generics.ListAPIView):
    serializer_class = salesOrderAndDtlSerializer
    lookup_field = 'companyId'
    permission_classes = (CompanyOwnerEditCancel, )

    def get_queryset(self):
        return salesOrder.objects.filter(companyId=self.kwargs['companyId'])


class getSalesOrderById(
        generics.RetrieveAPIView):
    serializer_class = salesOrderAndDtlSerializer
    queryset = salesOrder.objects.all()
    permission_classes = (CompanyOwnerEditCancel, )


""" GET REQUEST SALES ORDER DTL """
class getSalesOrdersDtl(
        generics.ListAPIView):
    serializer_class = salesOrderDtl
    lookup_field = 'companyId'
    permission_classes = (CompanyOwnerEditCancel, )

    def get_queryset(self):
        return salesOrderDtl.objects.filter(companyId=self.kwargs['companyId'])


class getSalesOrderDtlById(
        generics.RetrieveAPIView):
    serializer_class = salesOrderAndDtlSerializer
    queryset = salesOrderDtl.objects.all()
    permission_classes = (CompanyOwnerEditCancel, )


""" POST REQUEST  """

class insertSalesOrder(
    generics.CreateAPIView):
    serializer_class = salesOrderAndDtlSerializer
    queryset = salesOrder.objects.all()
    permission_classes = (CompanyOwnerEditCancel, )


class insertSalesOrderDtl(
    generics.CreateAPIView):
    serializer_class = salesOrderDtl
    queryset = salesOrderDtl.objects.all()
    permission_classes = (CompanyOwnerEditCancel, )

""" PUT/PATCH REQUEST """
class updateSalesOrderAndDtl(
    generics.UpdateAPIView):
    serializer_class = salesOrderAndDtlSerializer
    queryset = salesOrder.objects.all()
    lookup_field = 'pk'
    permission_classes = (CompanyOwnerEditCancel, )

    def get_object(self):
        obj = get_object_or_404(self.queryset, pk=self.request.data.get('pk'))
        self.check_object_permissions(self.request, obj)
        return obj
    
class updateSalesOrder(
    generics.UpdateAPIView):
    serializer_class = salesOrderSerializer
    queryset = salesOrder.objects.all()
    lookup_field = 'pk'
    permission_classes = (CompanyOwnerEditCancel, )

    def get_object(self):
        obj = get_object_or_404(self.queryset, pk=self.request.data.get('pk'))
        self.check_object_permissions(self.request, obj)
        return obj

class updateSalesOrderDtl(
    generics.UpdateAPIView):
    serializer_class = salesOrderDtlSerializer
    queryset = salesOrderDtl.objects.all()
    lookup_field = 'salesOrderId'
    permission_classes = (CompanyOwnerEditCancel, )

    def get_object(self):
        obj = get_object_or_404(self.queryset, salesOrderId=self.request.data.get('salesOrderId'))
        self.check_object_permissions(self.request, obj)
        return obj
    
class cancelSalesOrder(
        generics.UpdateAPIView):
    serializer_class = salesOrderSerializer
    queryset = salesOrder.objects.filter()
    permission_classes = (CompanyOwnerEditCancel,)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)       
        serializer.is_valid(raise_exception=True)      
        curr_company = salesOrder.objects.get(system_user_id=request.user.id)
        if curr_company.companyId == instance.companyId_id:
            serializer.validated_data['canceled'] = True
            self.perform_update(serializer)
            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}
            return Response(serializer.data)
        else:
            return Response('That Item doesnt exist in youre company!', status=status.HTTP_400_BAD_REQUEST)
    

