from django.shortcuts import redirect
from django.views import View
from django.views.generic import DetailView

from .models import ProfileCustomUser


class FollowView(View):

    def post(self, request, *args, **kwargs):
        my_profile = ProfileCustomUser.objects.get(email=request.user)
        author = request.POST.get('profile_pk')
        obj = ProfileCustomUser.objects.get(email=author)
        if obj in my_profile.following.all():
            my_profile.following.remove(obj)
            obj.follower.remove(my_profile.id)
        else:
            my_profile.following.add(obj)
            obj.follower.add(my_profile.id)

        return redirect(request.META.get('HTTP_REFERER'))


class ProfilesDetailView(DetailView):
    model = ProfileCustomUser
    template_name = 'post_detail.html'
