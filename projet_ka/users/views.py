from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.template import loader

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.core.mail import EmailMessage

from .forms import MyUserCreationForm, MyUserModifForm

# Create your views here.

"""class Registeruser(CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registeruser.html'"""

def Registeruser(request):
    if request.method == 'POST':
        form_reg = MyUserCreationForm(request.POST)
        if form_reg.is_valid():
            form_reg.save()
            username = form_reg.cleaned_data.get('email')
            raw_password = form_reg.cleaned_data.get('password1')
            user = authenticate(email=username, password=raw_password)
            login(request, user)
            message = 'à definir'
            mail_subject = "Création de votre compte Bokalia"
            user.email_user(mail_subject, message)
            #email = EmailMessage(mail_subject, message, to=[username])
            #email.send()
            return redirect('welcome')

    else:
        form_reg = MyUserCreationForm()

    return render(request, 'users/registeruser.html', {'form': form_reg})


@login_required()
def Profile(request):

    myuserf = MyUserModifForm(instance=request.user)
    chpass = PasswordChangeForm(user=request.user)

    if request.method == 'POST':
        myuserf = MyUserModifForm(request.POST, instance=request.user)

        if myuserf.is_valid():
            myuserf.save()
    else:
        myuserf = MyUserModifForm(instance=request.user)

    context = {
        'form_info': myuserf,
        'form_mdp' : chpass,
    }

    return render(request, 'users/profile.html', context)

"""@login_required()
def Profile(request):

    if request.method == 'POST':
        myuserf = MyUserModifForm(request.POST, instance=request.user)

        if myuserf.is_valid():
            myuserf.save()
    else:
        myuserf = MyUserModifForm(instance=request.user)

    context = {'form_info': myuserf}

    return render(request, 'users/profile.html', context)"""

"""def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
    else:
        ..."""
