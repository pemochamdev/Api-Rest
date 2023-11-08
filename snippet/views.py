from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from snippet.models import Snippet
from snippet.serializers import SnippetSerializer
# Create your views here.

#@csrf_exempt
@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    if request.method=='GET':

        snippets = Snippet.objects.all().order_by('-date_created')
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
            data = JSONParser().parse(request)
            serializer = SnippetSerializer(data=data)
            if serializer.is_va():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method=='GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)
    
    elif request.method=='PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

         

