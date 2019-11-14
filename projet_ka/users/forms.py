from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, UsernameField
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import check_password
from .models import MyUser
from django import forms

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
        fields = ('last_name', 'first_name', 'email', 'password1', 'password2', 'newsletter')
        field_classes = {'username': UsernameField}
        error_messages = {
            'email': {
                'unique': _("Cette adresse e-mail existe déjà"),
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #if self._meta.model.USERNAME_FIELD in self.fields:
        #   self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.update({'autofocus': True})
        for visible in self.visible_fields():
            visible.field.widget.attrs.update({'class': 'inptext'})
        self.fields['last_name'].widget.attrs.update({'autofocus': True})
        self.fields['newsletter'].widget.attrs.update({'class': 'inpcheck'})

class MyUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = MyUser
        fields = ('email',)

class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(label=_("E-MAIL"), widget=forms.TextInput(attrs={'autofocus': True, 'class': 'inptext', 'type': 'email', 'placeholder':'Adresse e-mail'}))
    password = forms.CharField(label=_("MOT DE PASSE"), strip=False, widget=forms.PasswordInput(attrs={'placeholder':'Mot de passe', 'class': 'inptext'}))

class MyUserModifForm(forms.ModelForm):
    typ_form = 1
    class Meta:
        model = MyUser
        fields = ('last_name', 'first_name', 'email', 'birth_date', 'newsletter')
        exclude = ('password',)
        widgets = {
            'birth_date': DateInput(),
        }
        error_messages = {
            'email': {
                'unique': _("Cette adresse e-mail existe déjà"),
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # if self._meta.model.USERNAME_FIELD in self.fields:
        #   self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.update({'autofocus': True})
        for visible in self.visible_fields():
            visible.field.widget.attrs.update({'class': 'inptext'})
        self.fields['newsletter'].widget.attrs.update({'class': 'inpcheck'})
        #self.fields['phone'].widget.input_type = 'tel'
        #self.fields['phone'].widget.attrs.update({'minlength': '10'})

class MyPasswordChangeForm(PasswordChangeForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=_('(Minimum 8 caractères)'),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # if self._meta.model.USERNAME_FIELD in self.fields:
        #   self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.update({'autofocus': True})
        for visible in self.visible_fields():
            visible.field.widget.attrs.update({'class': 'inptext'})
            visible.field.widget.attrs.update({'autofocus': False})
        #self.fields['new_password2'].help_text = 'zdaazd'
        #self.fields['phone'].widget.input_type = 'tel'
        #self.fields['phone'].widget.attrs.update({'minlength': '10'})

class ConfirmPasswForm(forms.ModelForm):
    confirm_password = forms.CharField(
        label=_("Confirmation de votre mot de passe"),
        widget=forms.PasswordInput(
            attrs= {'class': 'inptext'}
        ),
    )

    class Meta:
        model = MyUser
        fields = ('confirm_password',)

    def clean(self):
        cleaned_data = super(ConfirmPasswForm, self).clean()
        confirm_password = cleaned_data.get('confirm_password')
        if not check_password(confirm_password, self.instance.password):
            self.add_error('confirm_password', 'Le mot de passe saisie est invalide.')