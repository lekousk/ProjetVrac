from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template import loader

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required

from .forms import MyUserCreationForm

# Create your views here.

class Registeruser(CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registeruser.html'


@login_required()
def profile(request):
    return render()