from django.db import models
from django.utils import timezone

# Create your models here.

class Produit(models.Model):
	nom = models.CharField(max_length=40)
	cat = models.ForeignKey('Categorie_produit', on_delete = models.CASCADE) #Catégorie
	prix_p = models.FloatField(blank = True)
	type_prix = models.ForeignKey('Type_de_prix', on_delete = models.CASCADE)   #kg ou l ou pce
	date_saisie = models.DateTimeField(auto_now_add=True, verbose_name = "Date d'enregistrement du produit")
	date_der_modif = models.DateTimeField(verbose_name = "date de modification", auto_now=True, null = True, blank = True)
	# null autorise la valeur vide dans la BDD, blank autorise la saisie de vide dans la validation django ou formulaire

	description = models.TextField(null = True, blank = True)
	origine = models.CharField(max_length=30)
	ingredient = models.TextField(default= 'à remplir')
	conservation = models.TextField(null = True, blank = True)
	conseil_prepa =  models.TextField(null = True, blank = True)

	energie_kj = models.PositiveIntegerField(null = True, blank = True)
	energie_kcal = models.PositiveIntegerField(null = True, blank = True)
	matiere_grasse = models.DecimalField(null = True, blank = True, max_digits=7, decimal_places=2)
	acide_gras_sat = models.DecimalField(null = True, blank = True, max_digits=7, decimal_places=2)
	glucide = models.DecimalField(null = True, blank = True, max_digits=7, decimal_places=2)
	sucres = models.DecimalField(null = True, blank = True, max_digits=7, decimal_places=2)
	fibre_alim = models.DecimalField(null = True, blank = True, max_digits=7, decimal_places=2)
	proteine = models.DecimalField(null = True, blank = True, max_digits=7, decimal_places=2)
	sel = models.DecimalField(null = True, blank = True, max_digits=7, decimal_places=2)

	producteur = models.ForeignKey('Producteur', on_delete = models.CASCADE)
	image_p = models.ImageField(upload_to="image_produit/")

	class Meta:
		verbose_name = "produit"
		ordering = ['-date_saisie']

	def __str__(self):
		return self.nom

class Producteur(models.Model):
	nom = models.CharField(max_length=30)
	desc_prod = models.TextField()
	image_prod = models.ImageField(upload_to="image_producteur/")
	adresse1 = models.CharField(max_length=30)
	adresse2 = models.CharField(max_length=30, null = True)
	code_p = models.PositiveIntegerField()
	ville = models.CharField(max_length=20)
	tel_prod = models.PositiveIntegerField()
	email_prod = models.EmailField()
	nom_contact = models.CharField(max_length = 30)
	prenom_contact = models.CharField(max_length = 30)

	def __str__(self):
		return self.nom

class Categorie_mere(models.Model):
	nom = models.CharField(max_length = 40)

	def __str__(self):
		return self.nom

class Categorie_produit(models.Model):
	nom = models.CharField(max_length=30)
	cat_mere = models.ForeignKey('Categorie_mere', on_delete = models.CASCADE)

	def __str__(self):
		return self.nom

class Type_de_prix(models.Model):
	nom = models.CharField(max_length=20)

	def __str__(self):
		return self.nom


# Données pour les emballages: tous les types de bocal et kraft

class Emballage(models.Model):
	nom = models.CharField(max_length=30)	# Ex Bocal_xs / sachet_kraft
	taille = models.CharField(max_length=20)	# xs ou 0.5l ...
	hauteur = models.DecimalField(null = True, blank = True, max_digits=6, decimal_places=2,)
	diametre = models.DecimalField(null = True, blank = True, max_digits=6, decimal_places=2)
	prix = models.DecimalField(null = False, blank = False, max_digits=5, decimal_places=2)

	def __str__(self):
		return self.nom
