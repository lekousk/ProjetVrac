from django.contrib import admin
#from pages.models import Categorie, Article
from .models import Produit, Producteur, CategorieProduit, Emballage, CategorieMere, PrixUnite, Panier

admin.site.register(Produit)
admin.site.register(Producteur)
admin.site.register(CategorieProduit)
admin.site.register(Emballage)
admin.site.register(CategorieMere)
admin.site.register(PrixUnite)
admin.site.register(Panier)

# Register your models here.

"""class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date')
    list_filter = ('auteur', 'categorie',)
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('titre', 'contenu')
    
     # Configuration du formulaire d'édition
    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
       ('Général', {
            'classes': ['collapse', ],
            'fields': ('titre', 'auteur', 'categorie')
        }),
        # Fieldset 2 : contenu de l'article
        ('Contenu de l\'article', {
           'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !',
           'fields': ('contenu', )
        }),
    )

    # Colonnes personnalisées 
    def apercu_contenu(self, article):
        
        #Retourne les 10 premiers caractères du contenu de l'article. S'il
        #y a plus de 10 caractères, il faut rajouter des points de suspension.
        
        text = article.contenu[0:10]
        if len(article.contenu) > 10:
            return '%s…' % text
        else:
            return text
    
    # En en-tête de notre colonne
    apercu_contenu.short_description = 'Aperçu du contenu'"""

