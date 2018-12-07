from django.db import models
from django.utils import timezone

# Create your models here.

class Produit(models.Model):
	nom = models.CharField(max_length=40)
	cat = models.ForeignKey('Categorie_produit', on_delete = models.CASCADE) #Catégorie
	prix_p = models.FloatField()
	type_prix = models.ForeignKey('Type_de_prix', on_delete = models.CASCADE)   #kg ou litre ou qté
	date_saisie = models.DateTimeField(default = timezone.now, verbose_name = "Date d'enregistrement du produit")
	date_der_modif = models.DateTimeField(verbose_name = "date de modification", null = True) # pas obligatoire, en cas de modif
	desc_p = models.ForeignKey('Description', on_delete = models.CASCADE)
	producteur = models.ForeignKey('Producteur', on_delete = models.CASCADE)
	valeurs_nutri = models.ForeignKey('Valeurs_nutritionnelles', on_delete = models.CASCADE)
	image_p = models.ImageField(upload_to="image_produit/")

	class Meta:
		verbose_name = "produit"
		ordering = ['date_saisie']

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

class Description(models.Model):
	description = models.TextField()
	origine = models.CharField(max_length=30)
	ingredient = models.TextField()
	conservation = models.TextField()
	conseil_prepa =  models.TextField()

class Valeurs_nutritionnelles(models.Model):
	energie_kj = models.PositiveIntegerField()
	energie_kcal = models.PositiveIntegerField()
	matiere_grasse = models.PositiveIntegerField()
	acide_gras_sat = models.PositiveIntegerField()
	glucide = models.PositiveIntegerField()
	sucres = models.PositiveIntegerField()
	fibre_alim = models.PositiveIntegerField()
	proteine = models.PositiveIntegerField()
	sel = models.PositiveIntegerField()

class Categorie_produit(models.Model):
	nom = models.CharField(max_length=30)

	def __str__(self):
		return self.nom

class Type_de_prix(models.Model):
	nom = models.CharField(max_length=20)

	def __str__(self):
		return self.nom


""" class Provenance(models.Model):
	ville = models.CharField(max_length = 50, null = True)
	region = models.CharField(max_length = 50, null = True)
	pays = models.CharField(max_length = 50)
	groupe_pays = models.CharField(max_length = 50)

	def __str__(self):
		return self.ville

class ville(models.Model):
	ville = models.CharField(max_length = 50, null = True)

	def __str__(self):
		return self.ville

class region(models.Model):
	region = models.CharField(max_length = 50, null = True)

	def __str__(self):
		return self.region

class region(models.Model):
	region = models.CharField(max_length = 50, null = True)

	def __str__(self):
		return self.region """
