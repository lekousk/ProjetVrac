
// Attente du chargement entier du DOM

$(function() {

  /* JS */

  // Scroll up + A mettre dans la partie media queries > 1030px

  $(window).scroll(function () {
    if ($(this).scrollTop() > 180 ) {
      $('#scrollUp').show('slow');
    }
    else {
      $('#scrollUp').hide( 'slow' );
    }
  });


// comportement du panier au survol pour affichage de son contenu
var timeout;

$('.panier').on({
  mouseenter: function()
    {
    $('.panier_reduit').show();
    },
  mouseleave: function()
    {
    timeout = setTimeout(function()
      {
      $('.panier_reduit').hide();
      }, 200);
    }
});

// laisse le contenu ouvert à son survol
// le cache quand la souris sort
$('.panier_reduit').on({
  mouseenter: function() {
    clearTimeout(timeout);
  },
  mouseleave: function() {
    $('.panier_reduit').hide();
  }
});

// Récupérer les informations dans les cookies

nbrArticleDansPanier = parseInt(getCookie('nbrArticleDansPanier') ? getCookie('nbrArticleDansPanier') : 0);
articlesPanier = getCookie('articlesPanier') ? JSON.parse(getCookie('articlesPanier')) : [];

panier_vide_toggle();  // A activer !!!!!

// Afficher le nombre d'article du panier dans le widget

$('#nbr_article_dans_panier').html(nbrArticleDansPanier);

  // Articles trouvés dans le cookie
articlesPanier.forEach(function(v) {
  items += '<div class="classArticlePanier"><img src="' + 'data_img' + '"><div class="panier_milieu"><p class="panier_titre"><a href="' + v.url + '">' + v.nom + '</a><span> - ' + v.typ_pri + '</span></p><p class="panier_sousTitre">Poids (g) : <span>' + v.val_qte + '</span></p><p class="panier_sousTitre">Consigne comprise : <span>' + v.info_prix_emballage + '</span></p></div><div class="panier_prixArticle"><p><span>x </span>' + v.qt + '</p><p>' + v.prix_tot + '</p></div></div>';
});

  // Ajout des items dans le panier ul
$('.ajout_dans_panier').prepend(items);

});
//fin