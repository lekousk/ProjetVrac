import django_filters

from .models import Produit

class ProduitFiltrer(django_filters.FilterSet):
    nom = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Produit
        fields = ['nom', ]
