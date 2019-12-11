// Attente du chargement entier du DOM

// Ajouter dans la base de données:
// Les possibilités maximales de remplissage des bocaux et papier kraft suivant la taille:
// val_max_kraft_s / val_s_max pour le bocal S par ex

$(function() {

  //Test

  /*var width = $('.form_achat_produit').width();
  var height = $(window).height();
  var width_w = $(window).width();
 
     console.log(width + "  hauteur fenetre " + height + "    largeur fenetre " + width_w);*/

  // Initialisation des données:
  //$('#qte_input').val(0); // init quantité à 0

 // Calul du prix suivant la quantité
    // Initialisation des variables

var type_prix_article = $('.prix_produit').attr('info_type_prix');
var prix_article = parseFloat($('.prix_produit').attr('info_prix_produit').replace(",", "."));

    // Initialisation du prix de l'article pour les calcules

function calcul_prix(prix, type)
{
  if (type == 'kg')
  {
    prix = parseFloat(prix / 1000);
    return prix;
  }

  else
  {
    return prix;
  }
}

/* début calcul du prix des consignes */

var val_init = true;
var cste_qte, cste_prix;

if (val_init)
{
    prix_article = calcul_prix(prix_article, type_prix_article);

    $('.qte_consigne').each(function(cste_qte, cste_prix){
        cste_qte = parseFloat($(this).attr('data_qte_c'));
        cste_prix = parseFloat(cste_qte * prix_article).toFixed(2).replace(".", ",");
        $(this).next("p").children("span").text(cste_prix);
    });

    val_init = false;
}

/* Fin du calcul du prix des consignes */

// Début prix de l'emballage

var array_emballage=[];

$('.prix_emballage').each(function(i){
  i = $(this).attr('data_emballage');
  array_emballage[i] = $(this).text();
  //console.log(array_emballage[i]);
});

var taille_bocal = 0;
var taille_kraft = 0;

function afficer_prix_emballage(){
  if (cons_ou_kraft == 1)
  {
    if (taille_bocal == 1) //taille bocal, ici 1 = s
    {
      $('#affiche_prix_emballage').text(array_emballage['bocal_s']);
    }

    else if (taille_bocal == 2)
    {
      $('#affiche_prix_emballage').text(array_emballage['bocal_m']);
    }

    else if (taille_bocal == 3)
    {
      $('#affiche_prix_emballage').text(array_emballage['bocal_l']);
    }

    else if (taille_bocal == 4)
    {
      $('#affiche_prix_emballage').text(array_emballage['bocal_xl']);
    }

    else
    {
      $('#affiche_prix_emballage').text(array_emballage['sans']);
    }
  }

  else if (cons_ou_kraft == 2)
  {
    if (taille_kraft == 1) //taille bocal, ici 1 = s
    {
      $('#affiche_prix_emballage').text(array_emballage['kraft_s']);
    }

    else if (taille_kraft == 2)
    {
      $('#affiche_prix_emballage').text(array_emballage['kraft_m']);
    }

    else
    {
      $('#affiche_prix_emballage').text(array_emballage['sans']);
    }
  }

  else
  {
    $('#affiche_prix_emballage').text(array_emballage['sans']);
  }
}

function cache_emballage(taille_kraft, taille_bocal)
{
  if (taille_kraft == 0 && taille_bocal == 0)
  {
    $('.emballage_div').hide();
  }

  else
  {
    $('.emballage_div').show();
  }
}

// Fin prix emballage

// afficher l'option Kraft pour l'emballage

var cons_ou_kraft = 1;

$('.li_kraft').on({
  click: function() {
    var height_zc = $('.zone_choix').height();
    height_zc = height_zc + 'px';
    $('.zone_choix').css('min-height', height_zc);
    $('.zone_consigne').hide(200).queue(function(){
      $('.zone_kraft').show(200);
      $(this).dequeue();
    });

    $('.li_cons').animate({'border-bottom-width': '0px', 'opacity': '0.6'}, 100);
    $(this).animate({'border-bottom-width': "3px", 'opacity': '1'}, 100);
    $(this).off("mouseenter mouseleave"); // annuler le hover sur le passage de Kraft. 2e solution ? ($(this).unbind('mouseout mouseover')();)
    $(".li_cons").hover(function(){
      $(this).css("opacity", "1");
      }, 
      function(){
      $(this).css("opacity", "0.6");
      }
    );

    cons_ou_kraft = 2;

    //$('#qte_input').trigger("change"); // adapter le prix de l'emballage kraft lors de la selection en kraft
  }
});


// Revenir à l'option Consigne pour l'emballage

$('.li_cons').on({
  click: function() {
    $('.zone_kraft').hide(200).queue(function()
      {
        $('.zone_consigne').show(200);
        $(this).dequeue();
      }
    );
    $('.li_kraft').animate({'border-bottom-width': '0px', 'opacity': '0.6'}, 100);
    $(this).animate({'border-bottom-width': "3px", 'opacity': '1'}, 100);
    $(this).off("mouseenter mouseleave");
    $(".li_kraft").hover(function()
      {
        $(this).css("opacity", "1");
      },
      function()
      {
        $(this).css("opacity", "0.6");
      }
    );

    cons_ou_kraft = 1;
    //$('#qte_input').trigger("change"); // adapter la taille du local suivant la valeur choisie pendant la position de l'onglet en kraft
  }
});

// Afficher la description du producteur

$('#li_prod').on({
  click: function() {
    $('.art_desc').hide(200).queue(function()
      {
        $('.art_prod').show(200);
        $(this).dequeue();
      }
    );
    $('#li_desc').animate({'border-bottom-width': '0px', 'opacity': '0.6'}, 100);
    $(this).animate({'border-bottom-width': "3px", 'opacity': '1'}, 100);
    $(this).off("mouseenter mouseleave");
    $("#li_desc").hover(function()
      {
        $(this).css("opacity", "1");
      },
      function()
      {
        $(this).css("opacity", "0.6");
      }
    );
  }
});

// Revenir à la description du produit

$('#li_desc').on({
  click: function() {
    $('.art_prod').hide(200).queue(function()
      {
        $('.art_desc').show(200);
        $(this).dequeue();
      }
    );
    $('#li_prod').animate({'border-bottom-width': '0px', 'opacity': '0.6'}, 100);
    $(this).animate({'border-bottom-width': "3px", 'opacity': '1'}, 100);
    $(this).off("mouseenter mouseleave");
    $("#li_prod").hover(function()
      {
        $(this).css("opacity", "1");
      },
      function()
      {
        $(this).css("opacity", "0.6");
      }
    );
  }
});

// Initialisation taille Kraft

var val_max_kraft_s = 520;
var val_max_kraft_m = 1040;

function change_kraft(val_qte)
{
  if (0 < val_qte &&  val_qte <= val_max_kraft_s)
  {
    taille_kraft = 1;
  }
  else if (val_max_kraft_s < val_qte &&  val_qte <= val_max_kraft_m)
  {
    taille_kraft = 2;
  }
  else
  {
    taille_kraft = 0;
  }
}

// initialisation des quantités max pour chaque taille de bocal

var select_img_s = 0;

var etat_img_s = 0;

var val_s_max = parseInt($('#val_s_max').text()); // quantité de la valeur pleine du contenant S

var val_m_max = parseInt($('#val_m_max').text()); // quantité de la valeur pleine du contenant M

var val_l_max = parseInt($('#val_l_max').text()); // quantité de la valeur pleine du contenant L

var val_xl_max = parseInt($('#val_xl_max').text()); // quantité de la valeur pleine du contenant XL

$('#img_s').on({
  click: function()
    {
      $('#qte_input').val(val_s_max);
      $(this).attr({'src': "/static/boutique/images/leBocalTampon_plein.png"});
      $('#qte_input').trigger("change");
    }
});

$('#img_m').on({
  click: function()
    {
      $('#qte_input').val(val_m_max);
      $(this).attr({'src': "/static/boutique/images/leBocalTampon_plein.png"});
      $('#qte_input').trigger("change");
    }
});

$('#img_l').on({
  click: function()
    {
      $('#qte_input').val(val_l_max);
      $(this).attr({'src': "/static/boutique/images/leBocalTampon_plein.png"});
      $('#qte_input').trigger("change");
    }
});

$('#img_xl').on({
  click: function()
    {
      $('#qte_input').val(val_xl_max);
      $(this).attr({'src': "/static/boutique/images/leBocalTampon_plein.png"});
      $('#qte_input').trigger("change");
    }
});

$('#qte_input').on({
  change: function()
    {
      // changement des images bocal consigné

      var val_qte = parseInt($(this).val()); // quantité précise saisie
      change_qte(val_qte, val_s_max, val_m_max, val_l_max, val_xl_max);

      // Mise à jour du prix total

      var calc = calcul_prix(info_prix, val_qte, info_type).toFixed(2);

      $('#prix_cal').text(calc);

      // Mise à jour du prix de l'emballage
      change_kraft(val_qte);
      afficer_prix_emballage();
      cache_emballage(taille_kraft, taille_bocal);

    }
  });

function change_qte(val_qte, val_s_max, val_m_max, val_l_max, val_xl_max)
{
  if (val_qte == 0)
  {
    $('#img_s').attr({'src': "/static/boutique/images/leBocalTampon.png"});
    $('#img_m').attr({'src': "/static/boutique/images/leBocalTampon.png"});
    $('#img_l').attr({'src': "/static/boutique/images/leBocalTampon.png"});
    $('#img_xl').attr({'src': "/static/boutique/images/leBocalTampon.png"});
    taille_bocal = 0;
  }

  else if ( 0 < val_qte && val_qte <= val_s_max) 
  {
    $('#img_s').attr({'src': "/static/boutique/images/leBocalTampon_plein.png"});
    $('#img_m').attr({'src': "/static/boutique/images/leBocalTampon.png"});
    $('#img_l').attr({'src': "/static/boutique/images/leBocalTampon.png"});
    $('#img_xl').attr({'src': "/static/boutique/images/leBocalTampon.png"});
    taille_bocal = 1;
  }

  else if (val_s_max < val_qte && val_qte <= val_m_max) 
  {
    $('#img_m').attr({'src': "/static/boutique/images/leBocalTampon_plein.png"});
    $('#img_s').attr({'src': "/static/boutique/images/leBocalTampon.png"});
    $('#img_l').attr({'src': "/static/boutique/images/leBocalTampon.png"});
    $('#img_xl').attr({'src': "/static/boutique/images/leBocalTampon.png"});
    taille_bocal = 2;
  }

  else if (val_m_max < val_qte && val_qte <= val_l_max)
  {
    $('#img_l').attr({'src': "/static/boutique/images/leBocalTampon_plein.png"});
    $('#img_s').attr({'src': "/static/boutique/images/leBocalTampon.png"});
    $('#img_m').attr({'src': "/static/boutique/images/leBocalTampon.png"});
    $('#img_xl').attr({'src': "/static/boutique/images/leBocalTampon.png"});
    taille_bocal = 3;
  }

  else if (val_l_max < val_qte && val_qte <= val_xl_max) 
  {
    $('#img_xl').attr({'src': "/static/boutique/images/leBocalTampon_plein.png"});
    $('#img_s').attr({'src': "/static/boutique/images/leBocalTampon.png"});
    $('#img_m').attr({'src': "/static/boutique/images/leBocalTampon.png"});
    $('#img_l').attr({'src': "/static/boutique/images/leBocalTampon.png"});
    taille_bocal = 4;
  }

  else
  {
    $('#error_qte').show(200);
    $('#img_s').attr({'src': "/static/boutique/images/leBocalTampon.png"});
    $('#img_m').attr({'src': "/static/boutique/images/leBocalTampon.png"});
    $('#img_l').attr({'src': "/static/boutique/images/leBocalTampon.png"});
    $('#img_xl').attr({'src': "/static/boutique/images/leBocalTampon.png"});
    taille_bocal = 0;
  }
}

// Gestion des cookies

// Récupérer les informations dans les cookies

nbrArticleDansPanier = parseInt(getCookie('nbrArticleDansPanier') ? getCookie('nbrArticleDansPanier') : 0);
articlesPanier = getCookie('articlesPanier') ? JSON.parse(getCookie('articlesPanier')) : [];

// click bouton ajout panier

$('#ajout_panier').click(function() {
  
  // récupération des infos du produit
  var id = $(this).attr('data_id');
  var nom = $(this).attr('data_nom');
  var prix = $(this).attr('data_prix');
  var typ_pri = $(this).attr('data_type_prix'); // kg ou l ou pce
  var url = $(this).attr('data_url');
  var val_qte = parseInt($('#qte_input').val());
  var prix_tot = $('#prix_cal').text();
  var info_prix_emballage = parseFloat($('#affiche_prix_emballage').text().replace(",", "."));
  var qt = 1;
  
  nbrArticleDansPanier += qt;
  
  // mise à jour du nombre de produit dans le widget
  $('#nbr_article_dans_panier').html(nbrArticleDansPanier);
  
  var nouveauArticle = true;
  
  // vérifie si l'article est pas déjà dans le panier
  articlesPanier.forEach(function(v) {
    // si l'article est déjà présent, on incrémente la quantité
    if (v.id == id && v.val_qte == val_qte && v.info_prix_emballage == info_prix_emballage) {
      nouveauArticle = false;
      v.qt += qt;
      $('#'+ id).html('<div class="classArticlePanier"><img src="' + 'data_img' + '"><div class="panier_milieu"><p class="panier_titre"><a href="' + v.url + '">' + v.nom + '</a><span> - ' + v.typ_pri + '</span></p><p class="panier_sousTitre">Poids (g) : <span>' + v.val_qte + '</span></p><p class="panier_sousTitre">Consigne comprise : <span>' + v.info_prix_emballage + '</span></p></div><div class="panier_prixArticle"><p><span>x </span>' + v.qt + '</p><p>' + v.prix_tot + '</p></div></div>');
    }
  });
  
  // s'il est nouveau, on l'ajoute
  if (nouveauArticle) {
    
    articlesPanier.push({
      id: id,
      nom: nom,
      prix: prix,
      typ_pri: typ_pri,
      val_qte: val_qte,
      prix_tot: prix_tot,
      info_prix_emballage: info_prix_emballage,
      qt: qt,
      url: url
    });
    $('.ajout_dans_panier').prepend('<div class="classArticlePanier"><img src="' + 'data_img' + '"><div class="panier_milieu"><p class="panier_titre"><a href="' + url + '">' + nom + '</a><span> - ' + typ_pri + '</span></p><p class="panier_sousTitre">Poids (g) : <span>' + val_qte + '</span></p><p class="panier_sousTitre">Consigne comprise : <span>' + info_prix_emballage + '</span></p></div><div class="panier_prixArticle"><p><span>x </span>' + qt + '</p><p>' + prix_tot + '</p></div></div>');
  }
 
  // sauvegarde le panier -> fonction dans le fichier base_fonctions.js
  save_panier(nbrArticleDansPanier, articlesPanier);
 
  // affiche le contenu du panier si c'est le premier article -> fonction dans le fichier base_fonctions.js
  panier_vide_toggle();
});

});
//fin
