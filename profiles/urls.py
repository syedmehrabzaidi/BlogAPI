from django.urls import path
from .views import ProfilesDetailView, FollowView

app_name = 'profiles'

urlpatterns = [
    path('switch/', FollowView.as_view(), name='follow-unfollow-view'),
    path('<pk>/', ProfilesDetailView.as_view(), name='profile-detail-view'),

]
