from django.urls import path, re_path

from .views import (PostListCreateApiView,
                    PostDetailApiView,
                    UserSignUpView)


urlpatterns = [
    path('post/<int:pk>/', PostDetailApiView.as_view()),
    re_path(r'post/$', PostListCreateApiView.as_view()),
    path('post/signup/', UserSignUpView.as_view()),
]
