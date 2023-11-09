from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics


from snippet.models import Snippet
from snippet.serializers import SnippetSerializer
# Create your views here.

class SnippetList(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin, 
    generics.GenericAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request,  *args, **kwargs):
        return self.list(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
                
       return self.create(request, *args, **kwargs)
    

class SnippetDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return  self.retrieve(request, *args, **kwargs)

        
    def put(self,request, *args, **kwargs):

       return self.update(request, *args, **kwargs)
    
    
    def delete(self, request, *args, **kwargs):
      return self.destroy(request, *args, **kwargs)


