"""projet_ka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from .forms import CustomAuthForm


urlpatterns = [
    path('register', views.Registeruser, name='register'),
    #path('register/', views.Registeruser.as_view(template_name='users/registeruser.html'), name='register'),
    path('profile/', views.Profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html', authentication_form=CustomAuthForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/password_change/', views.MyPasswordChange, name='my_password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('deleteconfirmation', views.Delete_user, name='delete_confirmation'),
    path('Carnet_adresses', views.Carnet_adresses, name='Carnet_adresses'),
    path('adresse', views.New_Edit_adresse, name='new_adresse'),
    path('adresse/<int:num>', views.New_Edit_adresse, name='new_adresse'),
]
