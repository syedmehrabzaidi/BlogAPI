from .views import SignUpView, RegisterAPI

from django.urls import path


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('accounts_api', RegisterAPI.as_view()),
    ]
