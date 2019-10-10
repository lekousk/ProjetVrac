from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template import loader

from .forms import New_produit_F
from .models import Produit, Producteur, Emballage, Categorie_produit, Categorie_mere

# Create your views here.

def Accueil(request):

	return render(request, 'pages/accueil.html')


def Registeruser(request):
	form = New_produit_F(request.POST or None, request.FILES)

	if form.is_valid():
		nom_du_produit = form.cleaned_data['nom_du_produit']
		categorie = form.cleaned_data['categorie']
		prix_produit = form.cleaned_data['prix_produit']
		type_du_prix = form.cleaned_data['type_du_prix']
		date_saisie = form.cleaned_data['date_saisie']
		description = form.cleaned_data['description']
		image_produit = form.cleaned_data['image_produit']

		envoi = True

	else:
		form = New_produit_F()

	context = {
		'form': form,
	}

	# return render(request, 'boutique/edition.html', locals())
	return render(request, 'pages/registeruser.html', context)