
/* Avant l'attente du chargement du DOM */

/* Gestion des cookies */

// Fonction permettant d'enregistrer un cookie

function setCookie(cname, cvalue, exdays){
	if (exdays){

		var d= new Date();
		d.setTime(d.getTime() + (exdays*24*60*60*1000)); // (exdays) jours avant exipration
		var expires = "expires=" + d.toUTCString();
	}
	else var expires ="";

	// problème de caractères interdits : encodeURIComponent

	document.cookie = cname + "=" + encodeURIComponent(cvalue) + ";" + expires+';path=/';
}

// Fonction pour la récupération des cookies: analyse de tout les cookies pour trouver le notre

function getCookie(sname) {
	var sname = sname + "=";
	var cookContent = document.cookie, cookEnd, i, j;

	for (i = 0, c=cookContent.length; i<c; i++) {
		j = i + sname.length;

		if (cookContent.substring(i,j) == sname){
			cookEnd = cookContent.indexOf(";", j);
			if (cookEnd ==-1 ) {
				cookEnd = cookContent.length;
			}
			return decodeURIComponent(cookContent.substring(j,cookEnd));
		}
	}
}

/* récupération du cookie CSFR_token (csfrtoken) pour l'utilisation dans les fonctions POST de Ajax */

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    // fonction appelée avant d'envoyer une requête AJAX
    beforeSend: function(xhr, settings) {
        // on ajoute le header que si la requête de type POST est pas crossDomain
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

/* Gestion générale du panier */

// Variable pour stocker le nombre d'articles

var nbrArticleDansPanier;
var articlesPanier;

//Incrémentation du panier

var items ='';

// Sauvegarde du panier

function save_panier(nbrArticleDansPanier, articlesPanier){
	setCookie('nbrArticleDansPanier', nbrArticleDansPanier, 7);
	setCookie('articlesPanier', JSON.stringify(articlesPanier, 7));
}

// Afficher et/ou cacher les éléments du panier

function panier_vide_toggle() {
	if (nbrArticleDansPanier > 0){
		$('#panier_vide_msg').hide();
		$('#nbr_article_dans_panier').removeClass('hidden'); //Vérifier si ça marche l'affichage de l'icone nombre dans le panier
	}

	else {
		$('#panier_vide_msg').show();
		$('#nbr_article_dans_panier').addClass('hidden');
	}
}

/* Gestion affichage list ou mosaic des produits */
