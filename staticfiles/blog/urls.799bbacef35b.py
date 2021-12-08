from django.urls import path

from .views import (BlogListView, BlogDetailView,
                    BlogCreateView, BlogUpdateView,
                    BlogDeleteView, follower_list, following_list,
                    CommentCreateView, LikeView,
                    LikeViewHome, MyPDF, )

urlpatterns = [
    path(
        '',
        BlogListView.as_view(),
        name='home'
    ),
    path(
        'post/<int:pk>/',
        BlogDetailView.as_view(),
        name='post_detail'
    ),
    path(
        'blogpost-like/<int:pk>/', LikeView.as_view(),
        name="blogpost_like"
    ),

    path(
        r'^pdf/(?P<pk>\d+)/$',
        MyPDF.as_view(template_name='post_detail.html',
                      filename='post_pdf.pdf'),
        name='pdf-wk'
    ),

    path(
        'post/new/', BlogCreateView.as_view(),
        name='post_new'
    ),
    path(
        'comment/<int:pk>/', CommentCreateView.as_view(),
        name='post_comment'
    ),

    path(
        'post-like/<int:pk>', LikeViewHome.as_view(),
        name="post_like"
    ),
    path(
        'post/<int:pk>/edit/',
        BlogUpdateView.as_view(),
        name='post_edit'
    ),
    path(
        'post/<int:pk>/delete/',
        BlogDeleteView.as_view(),
        name='post_delete'
    ),

    path(
        'follower_list/',
        follower_list,
        name='follower-list'
    ),
    path(
        'following_list/',
        following_list,
        name='following-list'
    ),

]

