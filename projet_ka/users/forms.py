from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUser


class MyUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = MyUser
        fields = ('email', 'is_active', 'city')


class MyUserChangeForm(UserChangeForm):

    class Meta:
        model = MyUser
        fields = ('email', 'city',)