from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import ProfileCustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = ProfileCustomUser
        fields = ('email', )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = ProfileCustomUser
        fields = ('email', )
