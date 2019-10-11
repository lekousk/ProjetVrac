from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template import loader

# Create your views here.

def Accueil(request):

	return render(request, 'pages/accueil.html')
