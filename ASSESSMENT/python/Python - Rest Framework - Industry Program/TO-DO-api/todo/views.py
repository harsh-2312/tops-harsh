from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import Task
from .serializers import Taskserializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(["GET","POST"])
def task_list(request):
    if request.method=="GET":
        task_data = Task.objects.all()
        serializer = Taskserializer(task_data, many=True)
        return Response({
            'status': status.HTTP_200_OK,
            "data": serializer.data,
        })
    
    if request.method=="POST":
        jsondata = request.data
        serializer = Taskserializer(data=jsondata)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status":status.HTTP_201_CREATED,
                "data": serializer.data,
                "massege": "data created"
            })
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "error":serializer.errors
        })

@api_view(["GET","PUT","PATCH","DELETE"])
def task_details(request,id):
    try:
        task_data = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            'error': "data not found"
        })
    
    if request.method=='GET':
        serializer = Taskserializer(task_data)
        return Response({
            'status': status.HTTP_200_OK,
            "data": serializer.data,
        })
    
    if request.method=="PUT":
        jsondata = request.data
        serializer = Taskserializer(data=jsondata,instance=task_data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status":status.HTTP_201_CREATED,
                "data": serializer.data,
                "massege": "data update"
            })
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "error":serializer.errors
        })

    if request.method=="PATCH":
        jsondata = request.data
        serializer = Taskserializer(task_data,data=jsondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status":status.HTTP_201_CREATED,
                "data": serializer.data,
                "massege": "data update"
            })
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "error":serializer.errors
        })
    
    if request.method=="DELETE":
        task_data.delete()
        return Response({
            "status": status.HTTP_410_GONE,
            "message" : "data delete"
        })


        
        


