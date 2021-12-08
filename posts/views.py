from rest_framework import generics, permissions, status
from rest_framework.response import Response
import rest_framework_filters as filters
# from django_filters import rest_framework as filters

from blog.models import Post
from profiles.models import ProfileCustomUser
from .serializers import PostSerializer, UserSerializer


class ManagerPosts(filters.FilterSet):
    class Meta:
        model = Post
        fields = ['title']


class PostListCreateApiView(generics.ListCreateAPIView):
    filter_class = ManagerPosts
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserSignUpView(generics.ListCreateAPIView):
    queryset = ProfileCustomUser.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    def post(self, request, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
