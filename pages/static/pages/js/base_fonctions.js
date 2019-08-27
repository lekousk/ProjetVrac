
    // Avant l'attente du chargement du DOM

// Gestion des cookies

// Variable pour stocker le nombre d'articles

var nbrArticleDansPanier;
var articlesPanier;

//Incrémentation du panier

var items ='';

// Fonction permettant d'enregistrer un cookie

function setCookie(cname, cvalue){
  var d= new Date();
  d.setTime(d.getTime() + (7*24*60*60*1000)); // 7 jours  avant exipration
  var expires = "expires=" + d.toUTCString();

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

// Sauvegarde du panier

function save_panier(nbrArticleDansPanier, articlesPanier){
  setCookie('nbrArticleDansPanier', nbrArticleDansPanier);
  setCookie('articlesPanier', JSON.stringify(articlesPanier));
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

