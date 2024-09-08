from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CommentSerializer
from .serializers import Comment

@api_view(['GET']) # a decorator that allows the function to be accessed easily using http
def hello_world(request):
    # instance  
    comment = Comment(email="dan@gmail.com", content="playing with python")

    # serialize
    
    serializer = CommentSerializer(comment)
    serializer2 = CommentSerializer(data=serializer.data)
    if serializer2.is_valid():
        print(serializer.data)
    return Response({'data': serializer.data}) #extractign value from the serializer
    # serializer.save(comment, data=data)
    
  