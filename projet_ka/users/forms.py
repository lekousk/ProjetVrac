from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, UsernameField
from django.utils.translation import gettext_lazy as _
from .models import MyUser
from django import forms
from django.forms import Widget

class DateInput(forms.DateInput):
    input_type = 'date'

class MyUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Mot de passe"),
        strip=False,
        widget=forms.PasswordInput,
        help_text=("Minimum 8 caractères"),
    )
    password2 = forms.CharField(
        label=_("Confirmation du mot de passe"),
        widget=forms.PasswordInput,
        strip=False,
    )

    """birth_date = forms.DateField(
        label=_("date d'anniversaire"),
        widget=DateInput(),
    )"""

    class Meta:
        model = MyUser
        fields = ('last_name', 'first_name', 'phone', 'birth_date', 'email', 'password1', 'password2', 'adress', 'post_code', 'city', 'other_info','newsletter')
        field_classes = {'username': UsernameField}
        widgets = {
            'birth_date': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #if self._meta.model.USERNAME_FIELD in self.fields:
        #   self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.update({'autofocus': True})
        for visible in self.visible_fields():
            visible.field.widget.attrs.update({'class': 'inptext'})
        self.fields['last_name'].widget.attrs.update({'autofocus': True})
        self.fields['newsletter'].widget.attrs.update({'class': 'inpcheck'})
        self.fields['phone'].widget.input_type = 'tel'

class MyUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = MyUser
        fields = ('email',)

class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(label=_("E-MAIL"), widget=forms.TextInput(attrs={'autofocus': True, 'class': 'inptext', 'type': 'email', 'placeholder':'Adresse e-mail'}))
    password = forms.CharField(label=_("MOT DE PASSE"), strip=False, widget=forms.PasswordInput(attrs={'placeholder':'Mot de passe', 'class': 'inptext'}))
