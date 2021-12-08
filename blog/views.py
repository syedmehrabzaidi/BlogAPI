from wkhtmltopdf.views import PDFTemplateView

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)

from profiles.models import ProfileCustomUser
from .models import Post, Comments


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            my_profile = ProfileCustomUser.objects.get(email=self.request.user)
            user_count = my_profile.following.all().count()
            user_follower = my_profile.follower.all().count()
            res = (str(my_profile).split('@')[0]).upper()

            context["user_count"] = user_count
            context["user_follower"] = user_follower
            context["res"] = res
        return context


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        view_profile = Post.objects.get(pk=pk)
        return view_profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs.get("object").pk
        view_profile_post = Post.objects.get(pk=pk)
        author_id = view_profile_post.author.id
        author = ProfileCustomUser.objects.get(pk=author_id)
        follower_count = author.follower.all().count()
        following_count = author.following.all().count()
        try:
            my_profile = ProfileCustomUser.objects.get(email=self.request.user)
        except ProfileCustomUser.DoesNotExist:
            pass

        if view_profile_post.author in my_profile.following.all():
            check_follow = True
        else:
            check_follow = False

        likes_connected = get_object_or_404(Post, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['number_of_likes'] = likes_connected.number_of_likes()
        context['post_is_liked'] = liked

        context["follow"] = check_follow
        context["follower_count"] = follower_count
        context["following_count"] = following_count
        return context


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'body', 'image']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        # send_mail_func.delay(obj.author.id)
        return HttpResponseRedirect(self.success_url)


class CommentCreateView(CreateView):
    model = Comments
    template_name = 'comment.html'
    fields = ['comments']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.post = Post.objects.get(pk=self.kwargs.get('pk'))
        obj.save()
        pk = self.kwargs.get('pk')
        success_url = f'/post/{pk}/'
        return HttpResponseRedirect(success_url)


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body', 'image']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


class LikeView(View):
    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, id=request.POST.get('blogpost_id'))
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return redirect(request.META.get('HTTP_REFERER'))


class LikeViewHome(View):
    def post(self, request, *args, **kwargs):
        pk = kwargs['pk']
        post = get_object_or_404(Post, id=pk)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return redirect(request.META.get('HTTP_REFERER'))


class MyPDF(PDFTemplateView):
    template_name = 'templates/post_detail.html'

    def get_context_data(self, pk):
        context = {'post': Post.objects.get(pk=pk)}
        return context


def follower_list(request):
    return render(request, 'follower_list.html')


def following_list(request):
    return render(request, 'following_list.html')

