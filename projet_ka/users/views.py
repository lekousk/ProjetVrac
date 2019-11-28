from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.template import loader

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, login, authenticate
from .models import Address, ProfileCustomer

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
            """user.email_user(mail_subject, message) A re-selectionner !!!"""
            #email = EmailMessage(mail_subject, message, to=[username]) A supprimer
            #email.send() A supprimer
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
def New_Edit_adresse(request, num=None):
    succes_info_form = False
    profile = ProfileCustomer.objects.get(user__id=request.user.id)
    temp = True

    if num is not None:
        adress = get_object_or_404(Address, user=request.user, id=num)
    else:
        adress = Address(user=request.user)

    if request.method == 'POST':
        adress_form = NewAdresse(request.POST, instance=adress)
        if adress_form.is_valid():
            adress_form.save()
            if profile.adresse_defaut is None:
                profile.adresse_defaut = adress
                profile.save()
            return redirect('Carnet_adresses')
    else:
        adress_form = NewAdresse(instance=adress)

    context = {
        'form_adress': adress_form,
        'succes_info_form': succes_info_form,
        'temp': temp,
    }
    return render(request, 'users/adresse.html', context)

@login_required()
def Carnet_adresses(request):
    modif_type = request.GET.get('adt')
    modif_value = request.GET.get('adv')
    addressbook = Address.objects.filter(user__id__exact=request.user.id)
    profile = ProfileCustomer.objects.get(user__id=request.user.id)
    form_adress = True
    temp = 'ard'

    if profile.adresse_defaut:
        adresse_defaut = True
    else:
        adresse_defaut = False

    try:
        modif_type = int(modif_type)
        int(modif_value)
        modif_value = addressbook.get(id__exact=modif_value)
    except:
        modif_type = 0
        modif_value = 0

    if modif_type == 1:
        if profile.adresse_defaut == modif_value:
            adresse_defaut = False
        modif_value.delete()
    elif modif_type == 3:
        profile.adresse_defaut = modif_value
        profile.save()
        adresse_defaut = True

    if adresse_defaut:
        addressbook = addressbook.exclude(id__exact=profile.adresse_defaut.id)
        adresse_defaut = profile.adresse_defaut

    context = {
        'addresses_list': addressbook,
        'adresse_defaut': adresse_defaut,
        'form_adress': form_adress,
        'temp': temp,
    }
    return render(request, 'users/carnet_adresses.html', context)