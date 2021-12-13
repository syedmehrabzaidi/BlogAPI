from rest_framework import generics, permissions, status, request
from rest_framework.response import Response
# import rest_framework_filters as filters
from django_filters import rest_framework as filters
from django.db.models import Q

from blog.models import Post
from profiles.models import ProfileCustomUser
from .permissions import IsAuthorOrReadOnly, ApiPermissions, AuthorAllStaffAllButEditOrReadOnly
from .serializers import PostSerializer, UserSerializer


class PostFilter(filters.FilterSet):
    title = filters.CharFilter(method='my_custom_filter', label="title")
    body = filters.CharFilter(method='my_custom_filter', label="body")

    class Meta:
        model = Post
        # fields = {'title': ['icontains'], 'body': ['icontains'], }
        fields = ['title', 'body']

    def my_custom_filter(self, queryset, name, value):
        if self.request.GET['title'] == "" or self.request.GET['title'] != "":

            return Post.objects.filter(
                Q(title__icontains=self.request.GET['title']) | Q(body__contains=self.request.GET['body'])
            )
        else:
            return Post.objects.filter(
                Q(title__icontains=self.request.GET['title']) or Q(body__contains=self.request.GET['body'])
            )


class PostListCreateApiView(generics.ListCreateAPIView):
    filter_class = PostFilter
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserSignUpView(generics.ListCreateAPIView):
    queryset = ProfileCustomUser.objects.all()
    permission_classes = IsAuthorOrReadOnly
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
    # permission_classes = (AuthorAllStaffAllButEditOrReadOnly, )
