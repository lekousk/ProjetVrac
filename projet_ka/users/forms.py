from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.utils.translation import gettext_lazy as _
from .models import MyUser
from django import forms
from django.forms.widgets import TextInput


class MyUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
        help_text=("Minimum 8 caractères"),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta(UserCreationForm):
        model = MyUser
        #fields = '__all__'
        fields = ('email', 'first_name',)


class MyUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = MyUser
        fields = ('email',)

class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(label=_("E-MAIL"), widget=forms.TextInput(attrs={'autofocus': True, 'class': 'inptext', 'type': 'email', 'placeholder':'Adresse e-mail'}))
    password = forms.CharField(label=_("MOT DE PASSE"), strip=False, widget=forms.PasswordInput(attrs={'placeholder':'Mot de passe', 'class': 'inptext'}))
