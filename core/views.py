from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from .serializers import postSerializer
from .models import Post
from rest_framework import generics


class PostView(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        generics.GenericAPIView):
    serializer_class = postSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostCreateView(
    generics.ListCreateAPIView):
    serializer_class = postSerializer
    queryset = Post.objects.all()

    
""" class TestView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs): 
        qs = Post.objects.all()
        sr = postSerializer(qs, many=True)
        return  Response(sr.data)

    def post(self, request, *args, **kwargs):
        self.http_method_names.append("post")
        serializer = postSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors) """
