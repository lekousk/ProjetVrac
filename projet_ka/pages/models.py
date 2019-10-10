from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Customers(models.Model):
    registrenb = models.CharField(max_length=10)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=20)
    email
    pswd
    adresse
    phone
    birth
    user = models.OneToOneField(User)  # La liaison OneToOne vers le modèle User
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")
    signature = models.TextField(blank=True)
    inscrit_newsletter = models.BooleanField(default=False)

    def __str__(self):
        return self.nom