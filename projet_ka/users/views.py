from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.template import loader

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, login, authenticate
from .models import Address, MyUser

from .forms import MyUserCreationForm, MyUserModifForm, MyPasswordChangeForm, ConfirmPasswForm, NewAdresse, ProfileForm

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

    chpass_form = MyPasswordChangeForm(user=request.user)
    succes_info_form = False
    hidden = True

    if request.method == 'POST':
        myuser_form = MyUserModifForm(request.POST, instance=request.user)
        customer_form = ProfileForm(request.POST, instance=request.user.profile_customer)

        if myuser_form.is_valid() and customer_form.is_valid():
            myuser_form.save()
            customer_form.save()
            succes_info_form = True
    else:
        myuser_form = MyUserModifForm(instance=request.user)
        customer_form = ProfileForm(instance=request.user.profile_customer)

    context = {
        'form_myuser': myuser_form,
        'form_customer': customer_form,
        'form_mdp': chpass_form,
        'succes_info_form': succes_info_form,
        'cacher_hid': hidden,
    }

    return render(request, 'users/profile.html', context)

@login_required()
def MyPasswordChange(request):
    myuser_form = MyUserModifForm(instance=request.user)
    customer_form = ProfileForm(instance=request.user.profile_customer)
    hidden = False

    if request.method == 'POST':
        chpass_form = MyPasswordChangeForm(data=request.POST, user=request.user)
        update_session_auth_hash(request, chpass_form.user)
        if chpass_form.is_valid():
            chpass_form.save()
    else:
        chpass_form = MyPasswordChangeForm(user=request.user)

    context = {
        'form_myuser': myuser_form,
        'form_customer': customer_form,
        'form_mdp' : chpass_form,
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
            temp = 'Votre compte est prêt à être supprimé'
    else:
        conf_passw = ConfirmPasswForm()

    context = {
        'conf_passw': conf_passw,
        'temp': temp,
    }


    return render(request, 'users/delete.html', context)

@login_required()
def New_adresse(request):
    adress_form = NewAdresse()
    if request.method == 'POST':
        adress_form = NewAdresse(request.POST)
        if adress_form.is_valid():
            adresse_temp = adress_form.save(commit=False)
            adresse_temp.user = request.user
            adresse_temp.save()

    context = {
        'form_adress': adress_form,
    }
    return render(request, 'users/adresse.html', context)

@login_required()
def Carnet_adresses(request):
    addressbook = Address.objects.filter(user__exact=request.user)
    form_adress = True
    temp = request.user.id

    context = {
        'addresses_list': addressbook,
        'form_adress': form_adress,
        'temp': temp,
    }
    return render(request, 'users/carnet_adresses.html', context)