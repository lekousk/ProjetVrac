from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.template import loader

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.core.mail import EmailMessage

from .forms import MyUserCreationForm, MyUserModifForm, MyPasswordChangeForm, ConfirmPasswForm

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
            message = loader.render_to_string('users/created_email.html',{
                'user': user,
            })
            mail_subject = "Confirmation de votre inscription Bokalia"
            user.email_user(mail_subject, message)
            #email = EmailMessage(mail_subject, message, to=[username])
            #email.send()
            return redirect('welcome')

    else:
        form_reg = MyUserCreationForm()

    return render(request, 'users/registeruser.html', {'form': form_reg})


@login_required()
def Profile(request):

    chpass = MyPasswordChangeForm(user=request.user)
    succes_info_form = False
    hidden = True

    if request.method == 'POST':
        myuserf = MyUserModifForm(request.POST, instance=request.user)

        if myuserf.is_valid():
            myuserf.save()
            succes_info_form = True
    else:
        myuserf = MyUserModifForm(instance=request.user)

    context = {
        'form_info': myuserf,
        'form_mdp' : chpass,
        'succes_info_form': succes_info_form,
        'cacher_hid': hidden,
    }

    return render(request, 'users/profile.html', context)

@login_required()
def MyPasswordChange(request):
    myuserf = MyUserModifForm(instance=request.user)
    hidden = False

    if request.method == 'POST':
        chpass = MyPasswordChangeForm(data=request.POST, user=request.user)
        update_session_auth_hash(request, chpass.user)
        if chpass.is_valid():
            chpass.save()
    else:
        chpass = MyPasswordChangeForm(user=request.user)

    context = {
        'form_info': myuserf,
        'form_mdp' : chpass,
        'cacher_hid': hidden,
    }

    return render(request, 'users/profile.html', context)

@login_required()
def Delete_user(request):
    temp = 0
    if request.method == 'POST':
        conf_passw = ConfirmPasswForm(request.POST, instance=request.user)
        temp = request.POST

        if conf_passw.is_valid():
            temp = 'Profile prêt à être supprimé'
    else:
        conf_passw = ConfirmPasswForm()

    context = {
        'conf_passw': conf_passw,
        'temp': temp,
    }


    return render(request, 'users/delete.html', context)

"""def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
    else:
        ..."""
