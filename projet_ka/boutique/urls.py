"""projet_ka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('edition', views.NewProduitVue, name='edition'),
    path('all_product/', views.Rechercher, name='all_products'),
    path('produit/<int:id>', views.AffUnProduit, name='produit_solo'),
    path('add_panier', views.AddPanier, name='add_panier'),
    path('panier', views.Panier, name='panier'),
    path('add_fast/', views.AddFast, name='add_fast'),
]
