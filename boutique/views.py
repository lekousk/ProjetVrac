from django.shortcuts import render, get_object_or_404
from .forms import New_produit_F
from .models import Produit, Producteur, Emballage, Categorie_produit

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

	else:
		form = New_produit_F()

	#return render(request, 'boutique/edition.html', locals())
	return render(request, 'boutique/edition.html', {'form': form})

def Aff__tout_produits(request):

	produit = Produit.objects.all()

	return render(request, 'boutique/all_products.html', {'tout_produit': produit})

#def ex(id):
#	produit_x = Produit.objects.get(id=1)
#
#	if produit_x.type_prix == 'kg'
#
#	return produit_x.type_prix

def Aff_un_produit(request, id):
	produit_c = get_object_or_404(Produit, id=id)
	xc = produit_c.type_prix.nom
	emballage_tout = Emballage.objects.all()

	context = {
	'produit': produit_c,
	'emb_tout': emballage_tout,
	}

	if xc == 'kg':
		context['kraft_s'] = Emballage.objects.get(nom = 'kraft_s')
		context['kraft_m'] = Emballage.objects.get(nom = 'kraft_m')
		context['bocal_s'] = Emballage.objects.get(nom = 'bocal_s')
		context['bocal_m'] = Emballage.objects.get(nom = 'bocal_m')
		context['bocal_l'] = Emballage.objects.get(nom = 'bocal_l')
		context['bocal_xl'] = Emballage.objects.get(nom = 'bocal_xl')

	return render(request, 'boutique/lire.html', context)

def Panier(request):

	return render(request, 'boutique/panier.html')