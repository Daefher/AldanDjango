from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from company.models import (
    company
)
from part.permission import AuthorEditCancel
from .models import (
    part,
    partQty,
    partTran
)
from .serializers import (
    partSerializer,
)


class getParts(
        mixins.ListModelMixin,
        generics.GenericAPIView):
    serializer_class = partSerializer    
    lookup_field = 'companyId'

    def get_queryset(self):
        return part.objects.filter(companyId=self.kwargs['companyId'], canceled=False)

    def get(self, request, *args, **kwargs):
        result = self.list(request, *args, **kwargs)
        return result


class getAllParts(
        mixins.ListModelMixin,
        generics.GenericAPIView):
    serializer_class = partSerializer   
    lookup_field = 'companyId'

    def get_queryset(self):
        return part.objects.filter(companyId=self.kwargs['companyId'])

    def retreive(self, request, *args, **kwargs):
        result = self.list(request, *args, **kwargs)
        return result


class getPart(
        generics.RetrieveAPIView):
    serializer_class = partSerializer
    queryset = part.objects.all()


class insertPart(
        generics.CreateAPIView):
    serializer_class = partSerializer
    queryset = part.objects.all()
    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if company.objects.get(system_user_id=request.user.id).companyId == request.data.get('companyId'):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response('That Item doesnt exist in youre company!', status=status.HTTP_400_BAD_REQUEST)


class updatePart(
        generics.UpdateAPIView):
    serializer_class = partSerializer
    queryset = part.objects.all()
    permission_classes = (AuthorEditCancel,)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        curr_company = company.objects.get(system_user_id=request.user.id)
        if curr_company.companyId == instance.companyId_id:
            self.perform_update(serializer)
            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}
            return Response(serializer.data)
        else:
            return Response('That Item doesnt exist in youre company!', status=status.HTTP_400_BAD_REQUEST)


class cancelPart(
        generics.UpdateAPIView):
    serializer_class = partSerializer
    queryset = part.objects.filter()
    permission_classes = (AuthorEditCancel,)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)       
        serializer.is_valid(raise_exception=True)      
        curr_company = company.objects.get(system_user_id=request.user.id)
        if curr_company.companyId == instance.companyId_id:
            serializer.validated_data['canceled'] = True
            self.perform_update(serializer)
            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}
            return Response(serializer.data)
        else:
            return Response('That Item doesnt exist in youre company!', status=status.HTTP_400_BAD_REQUEST)
