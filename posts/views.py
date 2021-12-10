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
        return Post.objects.filter(
            Q(title__icontains=self.request.GET['title']) | Q(body__contains=self.request.GET['body'])
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
    permission_classes = (AuthorAllStaffAllButEditOrReadOnly, )



import logging
from django.utils.deprecation import MiddlewareMixin

import socket
import time
import json

request_logger = logging.getLogger('django.request')

# class RequestLogMiddleware(MiddlewareMixin):
#     """Request Logging Middleware."""
#
#     def __init__(self, *args, **kwargs):
#         """Constructor method."""
#         super().__init__(*args, **kwargs)

# def process_request(self, request):
#     """Set Request Start Time to measure time taken to service request."""
#     if request.method in ['POST', 'PUT', 'PATCH']:
#         request.req_body = request.body
#     if str(request.get_full_path()).startswith('/api/'):
#         request.start_time = time.time()
#
# def extract_log_info(self, request, response=None, exception=None):
#     """Extract appropriate log info from requests/responses/exceptions."""
#     log_data = {
#         'remote_address': request.META['REMOTE_ADDR'],
#         'server_hostname': socket.gethostname(),
#         'request_method': request.method,
#         'request_path': request.get_full_path(),
#         'run_time': time.time() - request.start_time,
#     }
#     if request.method in ['PUT', 'POST', 'PATCH']:
#         log_data['request_body'] = json.loads(
#             str(request.req_body, 'utf-8'))
#         if response:
#             if response['content-type'] == 'application/json':
#                 response_body = response.content
#                 log_data['response_body'] = response_body
#     return log_data
#
# def process_response(self, request, response):
#     """Log data using logger."""
#     if request.method != 'GET':
#         if str(request.get_full_path()).startswith('/api/'):
#             log_data = self.extract_log_info(request=request,
#                                              response=response)
#             request_logger.debug(msg='', extra=log_data)
#     return response
#
# def process_exception(self, request, exception):
#     """Log Exceptions."""
#     try:
#         raise exception
#     except Exception:
#         request_logger.exception(msg="Unhandled Exception")
#     return exception


# class SimpleMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         # One-time configuration and initialization.
#
#     def __call__(self, request):
#         # Code to be executed for each request before
#         # the view (and later middleware) are called.
#
#         response = self.get_response(request)
#
#         # Code to be executed for each request/response after
#         # the view is called.
#
#         return response
