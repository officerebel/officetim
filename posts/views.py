from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):

    queryset = Post.objects.all()

    serializer_class = PostSerializer
    parser_classes = (MultiPartParser, FormParser)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    parser_classes = (MultiPartParser, FormParser)

