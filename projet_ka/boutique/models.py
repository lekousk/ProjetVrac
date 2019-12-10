from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class Produit(models.Model):
    nom = models.CharField(_('Nom du produit'), max_length=40)
    cat = models.ForeignKey('CategorieProduit', null=True, on_delete=models.SET_NULL)  # Catégorie
    TYPE_DE_PRIX_CHOICES = [
        ('kg', 'kg'),
        ('l', 'l'),
        ('u', 'U'),
    ]
    prix_p = models.FloatField(_('Prix'), blank=True)
    type_prix = models.CharField(_('Type du prix'), max_length=3, choices=TYPE_DE_PRIX_CHOICES,
                                 default='kg')  # Kg ou L ou U
    date_saisie = models.DateTimeField(_("date d'enregistrement du produit"), auto_now_add=True)
    date_der_modif = models.DateTimeField(_('date de modification'), auto_now=True, null=True, blank=True)
    # null autorise la valeur vide dans la BDD, blank autorise la saisie de vide dans la validation django ou formulaire

    description = models.TextField(_('Description'), null=True, blank=True)
    origine = models.CharField(_('Origine'), max_length=30)
    ingredient = models.TextField(_('Ingrédient'), default='à remplir')
    conservation = models.TextField(_('Conseil de conservation'), null=True, blank=True)
    conseil_prepa = models.TextField(_('Conseil de préparation'), null=True, blank=True)

    energie_kj = models.PositiveIntegerField(_('Valeur Energétique en Kj'), null=True, blank=True)
    energie_kcal = models.PositiveIntegerField(_('Valeur Energétique en Kcal'), null=True, blank=True)
    matiere_grasse = models.DecimalField(_('Matières grasses'), null=True, blank=True, max_digits=7, decimal_places=2)
    acide_gras_sat = models.DecimalField(_('Acides gras saturés'), null=True, blank=True, max_digits=7,
                                         decimal_places=2)
    glucide = models.DecimalField(_('Glucides'), null=True, blank=True, max_digits=7, decimal_places=2)
    sucres = models.DecimalField(_('dont sucres'), null=True, blank=True, max_digits=7, decimal_places=2)
    fibre_alim = models.DecimalField(_('Fibres alimentaires'), null=True, blank=True, max_digits=7, decimal_places=2)
    proteine = models.DecimalField(_('Protéines'), null=True, blank=True, max_digits=7, decimal_places=2)
    sel = models.DecimalField(_('Sel'), null=True, blank=True, max_digits=7, decimal_places=2)

    producteur = models.ForeignKey('Producteur', null=True, on_delete=models.SET_NULL)
    image_p = models.ImageField(_('Image du produit'), upload_to="boutique/image_produit/", null=True, blank=True)

    class Meta:
        verbose_name = "produit"
        ordering = ['-date_saisie']

    def __str__(self):
        return self.nom


class Producteur(models.Model):
    nom = models.CharField(_('Nom du producteur'), max_length=30)
    desc_prod = models.TextField(_('Description'), null=True, blank=True)
    image_prod = models.ImageField(_('Image du producteur'), upload_to="boutique/image_producteur/", null=True,
                                   blank=True)
    adresse1 = models.CharField(_('Adresse n°1'), max_length=30, null=True, blank=True)
    adresse2 = models.CharField(_('Adresse n°2, facultative'), max_length=30, null=True, blank=True)
    code_p = models.PositiveIntegerField(_('Code postal'), null=True, blank=True)
    ville = models.CharField(_('Ville'), max_length=20, null=True, blank=True)
    tel_prod = models.PositiveIntegerField(_('Téléphone'), null=True, blank=True)
    email_prod = models.EmailField(_('Adresse e-mail'), null=True, blank=True)
    nom_contact = models.CharField(_('Nom du contact'), max_length=30, null=True, blank=True)
    prenom_contact = models.CharField(_('Prénom du contact'), max_length=30, null=True, blank=True)

    def __str__(self):
        return self.nom


class CategorieMere(models.Model):
    nom = models.CharField(max_length=40)

    def __str__(self):
        return self.nom


class CategorieProduit(models.Model):
    nom = models.CharField(max_length=30)
    cat_mere = models.ForeignKey(CategorieMere, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


# Données pour les emballages: tous les types de bocal et kraft

class Emballage(models.Model):
    nom = models.CharField(max_length=30)  # Ex Bocal_xs / sachet_kraft
    taille = models.CharField(max_length=20)  # xs ou 0.5l ...
    hauteur = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2, )
    diametre = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2)
    prix = models.DecimalField(null=False, blank=False, max_digits=5, decimal_places=2)

    class Meta:
        ordering = ['nom',]

    def __str__(self):
        return self.nom


class PrixUnite(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='prix_unite')
    ordre_p = models.IntegerField(_('Order du produit'))
    emballage = models.ForeignKey(Emballage, on_delete=models.CASCADE, related_name='emballage')
    quantite = models.IntegerField(_('Quantité du contenant'))
    unite = models.CharField(max_length=5, null=True, blank=True)

    class Meta:
        ordering = ['produit', 'ordre_p']

    def __str__(self):
        return '%s - %s' % (self.produit, self.emballage)
