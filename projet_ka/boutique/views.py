from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView
from django.db.models import Q, Count
from django.http import JsonResponse
from django.template import loader

from .forms import NewProduitForm
from .models import Produit, Producteur, Emballage, CategorieProduit, CategorieMere
from .filters import ProduitFiltrer


# Create your views here.

def NewProduitVue(request):
    form = NewProduitForm(request.POST or None, request.FILES)

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
        form = NewProduitForm()

    # return render(request, 'boutique/edition.html', locals())
    return render(request, 'boutique/edition.html', {'form': form})


def Rechercher(request):
    paginate = False
    prod_list = False
    query = request.GET.get('query')
    trier = request.GET.get('tr')
    filtre = request.GET.get('fi')
    rayon = request.GET.get('ray')
    prod_list = Produit.objects.filter(Q(nom__icontains=query) | Q(ingredient__icontains=query))
    prod_list_filtre = prod_list
    filtreStr = str(filtre)
    fiCat = False
    fiProd = False
    searchProd = False
    searchRay = False
    filtreOk = True
    rayonOk = True
    temp = 'pas attribué'

    noms = prod_list

    # Création de la liste des Rayons
    if len(prod_list) > 0:
        tempListeStr = []

        # Création de la liste des items choisi, suivant le filtre appliqué
        for d in list(prod_list.values('cat__cat_mere')):
            for e in d.values():
                tempListeStr.append("cat " + str(e))

        tempDict = {}.fromkeys(set(tempListeStr), )
        for f in set(tempListeStr):
            j = f.split()
            tempListeNb = []

            # Création de la liste des items choisi, suivant le filtre appliqué
            for k in list(prod_list.filter(cat__cat_mere__exact=int(j[1])).values('cat')):
                for l in k.values():
                    tempListeNb.append(CategorieProduit.objects.get(id=l))
            # Création d'un Dict avec quels filtres présents et l'occurence
            compteFiltre = {}.fromkeys(set(tempListeNb), 0)
            for g in tempListeNb:
                compteFiltre[g] += 1
            tempDict[f] = compteFiltre
        fiCat = tempDict

    # Affichage des résultats quand un ou plusieurs rayons sont sélectionnés
    # test de la consigne rayon si présente
    try:
        len(rayon)
    except:
        rayon = ""
    if len(rayon) > 0:
        rayListStr = rayon.split(',')
        rayListNb = []
        for a in rayListStr:
            try:
                int(a)  # Test si a peut être n nombre, sinon la consigne filtre n'est pas bonne
                rayListNb.append(int(a))
            except:
                rayonOk = False
                rayon = ""
        # temp = prod_list.filter(cat__id__in = rayListNb)
        if rayonOk:
            prod_list = prod_list.filter(cat__id__in=rayListNb)
            searchRay = CategorieProduit.objects.filter(id__in=rayListNb)

    # Création de la liste des Producteurs
    if len(prod_list) > 0:
        # Création de la liste des producteurs
        tempListe1 = []
        for d in list(prod_list.values('producteur__nom')):
            for e in d.values():
                tempListe1.append(str(e))

        tempDict1 = {}.fromkeys(set(tempListe1), )
        for f in set(tempListe1):
            tempListeNb1 = []

            # Création de la liste des items choisi, suivant le filtre appliqué ET UTILISATION de prod_list_filtre pour filtrer par rapport à Query
            for k in list(prod_list_filtre.filter(producteur__nom__exact=f).values('producteur')):
                for l in k.values():
                    tempListeNb1.append(Producteur.objects.get(id=l))
            # Création d'un Dict avec quels filtres présents et l'occurence
            compteFiltre1 = {}.fromkeys(set(tempListeNb1), 0)
            for g in tempListeNb1:
                compteFiltre1[g] += 1
            tempDict1[f] = compteFiltre1
        fiProd = tempDict1

    # Affichage des résultats quand un ou plusieurs filtres sont sélectionnés
    # test de la consigne filtre si présente
    try:
        len(filtre)
    except:
        filtre = ""
    if len(filtre) > 0:
        fiListStr = filtre.split(',')
        fiListNb = []
        for a in fiListStr:
            try:
                int(a)  # Test si a peut être n nombre, sinon la consigne filtre n'est pas bonne
                fiListNb.append(int(a))
            except:
                filtreOk = False
                filtre = ""
        # temp = prod_list.filter(cat__id__in = rayListNb)
        if filtreOk:
            prod_list = prod_list.filter(producteur__id__in=fiListNb)
            searchProd = Producteur.objects.filter(id__in=fiListNb)

    # Affichage des résultats suivant le tri sélectionné
    # test de la consigne trier si présente
    try:
        len(trier)
    except:
        trier = ""
    if len(trier) > 0:
        trier = int(trier)
        if trier == 2:
            prod_list = prod_list.order_by('prix_p')
            temp = 'val 2'
        elif trier == 3:
            prod_list = prod_list.order_by('-prix_p')
            temp = 'val 3'
        elif trier == 4:
            prod_list = prod_list.order_by('producteur')
        elif trier == 5:
            prod_list = prod_list.order_by('-producteur')

    # Définition de la pagination
    if prod_list:
        p = Paginator(prod_list, 6)
        page = request.GET.get('page', 1)
        nbresult = len(prod_list)
        try:
            prod_list = p.page(page)
        except PageNotAnInteger:
            prod_list = p.page(1)
        except EmptyPage:
            prod_list = p.page(p.num_pages)
        if p.num_pages > 1:
            paginate = True

    context = {
        'produit': prod_list,
        'noms': noms,
        'paginate': paginate,
        'tr': trier,
        'fi': filtre,
        'ray': rayon,
        'query': query,
        'temp': temp,
        'fiCat': fiCat,
        'fiProd': fiProd,
        'searchProd': searchProd,
        'searchRay': searchRay,
    }
    return render(request, 'boutique/all_products.html', context)


def AffUnProduit(request, id):
    produit_c = get_object_or_404(Produit, id=id)
    xc = produit_c.type_prix.nom
    emballage_tout = Emballage.objects.all()

    context = {
        'produit': produit_c,
        'emb_tout': emballage_tout,
    }

    if xc == 'kg':
        context['kraft_s'] = Emballage.objects.get(nom='kraft_s')
        context['kraft_m'] = Emballage.objects.get(nom='kraft_m')
        context['bocal_s'] = Emballage.objects.get(nom='bocal_s')
        context['bocal_m'] = Emballage.objects.get(nom='bocal_m')
        context['bocal_l'] = Emballage.objects.get(nom='bocal_l')
        context['bocal_xl'] = Emballage.objects.get(nom='bocal_xl')

    return render(request, 'boutique/lire.html', context)


def Panier(request):
    return render(request, 'boutique/panier.html')


def AddFast(request):
    link = request.GET.get('link')
    prod_ch = get_object_or_404(Produit, id=link)

    addfast_html = loader.render_to_string(
        'boutique/add_rapid.html',
        {'prod_ch': prod_ch}
    )
    # package output data and return it as a JSON object
    output_data = {
        'addfast_html': addfast_html,
    }

    return JsonResponse(output_data)
