from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Globalnote
from .serializers import Globalnoteserializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def globalenotelist(request):
    try:
        if request.method == "GET":
            student = Globalnote.objects.all()
            serializer = Globalnoteserializer(student, many=True)
            data = {
                "data" : serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)
        elif request.method == "POST":
            jsonedata = request.data
            serializer = Globalnoteserializer(data=jsonedata)
            if serializer.is_valid():
                serializer.save()
                data = {
                    "data" : serializer.data,
                }
                return Response(data, status=status.HTTP_201_CREATED)
            else:
                data = {
                    "error" : serializer.errors
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'error': str(e)
        })
    
@api_view(['GET','PUT','PATCH','DELETE'])
def globaleNotesDetails(request,id):
    try:
        student_ = Globalnote.objects.get(id=id)
    except Globalnote.DoesNotExist:
        return Response({
            'status':status.HTTP_204_NO_CONTENT,
            'massege':'data not found '
        })
    if request.method=="GET":
        serializer = Globalnoteserializer(instance=student_)
        return Response({
            'status': status.HTTP_200_OK,
            'data':serializer.data
        })
    if request.method=="PUT":
        jsondata = request.data
        serializer=Globalnoteserializer(instance=student_,data=jsondata)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status':status.HTTP_202_ACCEPTED,
                'data':serializer.data,
                'massege':" Change Successfully"
            })
        else:
            return Response({
                "status":status.HTTP_400_BAD_REQUEST,
                'error':serializer.errors
            })
    if request.method=="PATCH":
        jsondata = request.data
        serializer=Globalnoteserializer(instance=student_,data=jsondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status':status.HTTP_202_ACCEPTED,
                'data':serializer.data,
                'massege':"Student Comment Change Successfully Partially"
            })
        else:
            return Response({
                "status":status.HTTP_400_BAD_REQUEST,
                'error':serializer.errors
            })
    else:
        student_.delete()
        return Response({
            "status_code" : status.HTTP_410_GONE,
            "message" : "Comment Deleted Successfully"
        })

@api_view(["GET"])
def studentglobelnote(request,student_id):
    studentdata = Globalnote.objects.filter(student_id=student_id)
    if request.method =="GET":
        if studentdata:
            serializer = Globalnoteserializer(studentdata,many=True)
            data = {
                'data':  serializer.data
            }
            return Response(data,status=status.HTTP_200_OK)
        else:
            data={
                'error': 'data not found'
            }
            return Response(data,status=status.HTTP_400_BAD_REQUEST)
    else:
        data = {
            "error" : "Something Went Wrong"
        }
        return Response(data,status=status.HTTP_400_BAD_REQUEST)

        