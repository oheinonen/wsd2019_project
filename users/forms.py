from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

usertypes = (
    ("dev", "developer"),
    ("player", "player")
)


class CustomUserCreationForm(UserCreationForm):
    usertype = forms.MultipleChoiceField(choices=usertypes)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'usertype')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'usertype')
