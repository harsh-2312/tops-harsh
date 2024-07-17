
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import Bookserializers

@api_view(["GET", "POST"])
def booklist(request):
    if request.method == "GET":
        bookqueryset = Book.objects.all()
        serializer = Bookserializers(bookqueryset, many=True)
        return Response({
            "status": status.HTTP_200_OK,
            "payload": serializer.data
        })

    if request.method=="POST":
        serializer = Bookserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": status.HTTP_201_CREATED,
                "payload" : serializer.data,
                "message":'data created'
            })
        
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "error": serializer.errors
        })

@api_view(['GET','PUT','PATCH','DELETE'])
def  book_details(request,book_id):
    try:
        bookqueryset = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return Response({
            "status":status.HTTP_400_BAD_REQUEST,
            "message" : "book not found"
        })
    
    if request.method=="GET":
        serializer = Bookserializers(bookqueryset)
        return Response({
            "status": status.HTTP_200_OK,
            "paylode": serializer.data
        })
    
    elif request.method=="PUT":
        serializer = Bookserializers(bookqueryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": status.HTTP_201_CREATED,
                "paylode":serializer.data,
                "message":"book data update"
            })
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "error":serializer.errors
        })
    
    elif request.method == "PATCH":
        serializer = Bookserializers(bookqueryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": status.HTTP_201_CREATED,
                "payload": serializer.data,
                "message": "update data"
            })
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "error": serializer.errors
        })
    
    elif request.method=="DELETE":
        bookqueryset.delete()
        return Response({
            "status": status.HTTP_410_GONE,
            "message" : "data delete"
        })
