from django.shortcuts import render, get_object_or_404, HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView
from django.db.models import Q, Count
from django.http import JsonResponse
from django.template import loader
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.serializers import serialize, deserialize
import json

from .forms import NewProduitForm
from .models import Produit, Producteur, Emballage, CategorieProduit, CategorieMere, PrixUnite, Panier
from .filters import ProduitFiltrer


# Create your views here.
@ensure_csrf_cookie
def AffUnProduit(request, id):
    produit_c = get_object_or_404(Produit, id=id)
    prix_unite = PrixUnite.objects.filter(produit__id__exact=produit_c.id)
    #request.session['ok'] = True

    context = {
        'produit': produit_c,
        'prix_u': prix_unite,
    }

    return render(request, 'boutique/produit_solo.html', context)

def AddPanier(request):
    #addpanier_html = 'init'

    """exemple:

    @csrf_exempt
    def check_auth(request):
        if request.method == 'POST':
            print(request.user)
            if request.user.is_authenticated():
                content = {'message': 'Authenticated'}
                response = JsonResponse(content, status=200)
                return response
            else:
                content = {'message': 'Unauthenticated'}
                response = JsonResponse(content, status=401)
                return response"""

    if request.user.is_authenticated and request.method == 'POST':
        #addpanier_html = request.POST
        data_produit = request.POST.get('data_produit')
        data_consigne = request.POST.get('data_consigne')
        qte_input = request.POST.get('qte_input')

        if data_consigne == '1':
            prix_unite = PrixUnite.objects.filter(Q(produit__id=int(data_produit)) & Q(quantite__gte=int(qte_input))).first()
            consigne = prix_unite.emballage
        elif data_consigne == '2':
            consigne = Emballage.objects.get(nom = 'aucun')
        else:
            consigne = 'marde'

        #test = Produit.objects.get(id = int(data_produit))
        panier, obj = Panier.objects.get_or_create(
            user = request.user,
            produit = Produit.objects.get(id = int(data_produit)),
            emballage = consigne,
            quantite = int(qte_input),
            defaults = {'nb': 1},
        )

        if not obj: #obj à True si le panier est créé, donc on incrémente si False
            panier.nb += 1
            panier.save()

        output_data = {
            'addpanier_html': str(panier),
        }
    else:
        output_data = {
            'addpanier_html': 'pas authentifié',
        }

    return JsonResponse(output_data)

"""cookie = request.COOKIES
list_cookie = []

for key in cookie:
    if 'basket' in key:
        list_cookie.append(key)

val_panier = {
    'pro': int(data_produit),
    'emb': int(data_consigne),
    'qte': int(qte_input),
    'nb': 1,
}
panier = json.dumps(val_panier)
output_data = {
    'addpanier_html': panier,
}
response = JsonResponse(output_data)
response.set_cookie('Basket' + '1', value=panier)
#panier = json.loads(panier)
#panier = panier['emballage']
#panier = panier.content

return response"""

"""def AddFast(request):
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

    return JsonResponse(output_data)"""

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

@ensure_csrf_cookie
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
