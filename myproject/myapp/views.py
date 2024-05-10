from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Comment
from .serializers import CommentSerializer

# Create your views here.

# Logic for Read
@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        comment_obj = Comment.objects.all()
        serializer = CommentSerializer(comment_obj, many=True)
        return Response(serializer.data,status=200)

# Logic for Read perticular id 
@api_view(['GET']) 
def comments(request,id):
    if request.method == "GET":
        comment_obj= Comment.objects.get(id=id)
        comment_seri= CommentSerializer(comment_obj)

        return Response(comment_seri.data)
    
# Logic for Create
@api_view(['POST'])
def create_list(request):
    serializer = CommentSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors,status=400)


# Logic for Update
@api_view(['GET','PUT']) 
def update_list(request,id):
    try:
        comment_obj= Comment.objects.get(id=id)
    except Comment.DoesNotExist:
        return Response(status=404)
    
    # This using data get
    if request.method == "GET":
        comment_obj= Comment.objects.get(id=id)
        comment_seri= CommentSerializer(comment_obj)
        return Response(comment_seri.data)
    
    # This using data update
    elif request.method == "PUT":
        serializer = CommentSerializer(comment_obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    

# Logic for Delete
@api_view(['GET','DELETE']) 
def delete_list(request,id):
    try:
        comment_obj= Comment.objects.get(id=id)
    except Comment.DoesNotExist:
        return Response(status=404)
    
    # This using data get
    if request.method == "GET":
        comment_obj= Comment.objects.get(id=id)
        comment_seri= CommentSerializer(comment_obj)
        return Response(comment_seri.data)
    
    # This using data delete
    elif request.method == 'DELETE':
        comment_obj.delete()
        return Response({'message': 'Record deleted successfully'},status=204)


    
