from django.shortcuts import render
from .forms import New_produit_F

# Create your views here.

def New_produit_vue(request):

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

	return render(request, 'boutique/edition.html', locals())