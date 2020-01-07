// Attente du chargement entier du DOM

// Ajouter dans la base de données:

$(function() {

  //Test

  /*var width = $('.form_achat_produit').width();
  var height = $(window).height();
  var width_w = $(window).width();
 
     console.log(width + "  hauteur fenetre " + height + "    largeur fenetre " + width_w);*/

/* Début Initialisation du prix de l'article pour les calcules */

var type_prix_article = $('.prix_produit').attr('info_type_prix');
var prix_article = parseFloat($('.prix_produit').attr('info_prix_produit').replace(",", "."));
var unite_calcul = $('.consigne_column').first().attr('data_unite');

function calcul_prix(prix, type, unite)
{
  if (type != unite && type == 'kg')
  {
    prix = parseFloat(prix / 1000);
    return prix;
  }

  else
  {
    return prix;
  }
}

/* Fin Initialisation du prix de l'article pour les calcules */

/* début calcul du prix des consignes - INITIALISATION */

var val_init = true;
var cste_qte, cste_prix, qte_max;

if (val_init)
{
    prix_article = calcul_prix(prix_article, type_prix_article, unite_calcul);

    // Calcul des prix de bocaux
    $('.qte_consigne').each(function(cste_qte, cste_prix){
        cste_qte = parseFloat($(this).attr('data_qte_c'));
        cste_prix = parseFloat(cste_qte * prix_article).toFixed(2);
        $(this).next("p").children("span").text(cste_prix.replace(".", ","));
    });

    qte_max = parseInt($('.qte_max').attr('data_qte_max'));
    $('#qte_input').attr('max', qte_max);

    // valeurs initiales des prix emballages et des paliers pour le changement de bocal

    var tab_consigne= new Array();

    $('.consigne_column').each(function(i){
      i = $(this).attr('id_consigne');
      tab_consigne[i] = $(this).children('.qte_consigne').attr('data_qte_c');
    });

    // Initialisation: option 1: Consigne
    var cons_kraft = 1;

    val_init = false;
}

/* Fin du calcul du prix des consignes - INITIALISATION */

/* Début changement d'image du bocal en survole */

var cste_init, cste_vide, cste_plein;

$('.consigne_image').on({
    mouseenter: function(){
        cste_plein = $(this).attr('data_plein');
        cste_init = $(this).attr('src');
        $(this).attr('src', cste_plein);
    },
    mouseleave: function(){
        $(this).attr('src', cste_init);
    },
    click: function(){
        var cste_local = $(this).next('.qte_consigne').attr('data_qte_c');
        var cste_local2 = $(this).parent().attr('id_consigne');
        //ChangeIcone(cste_local2);
        $('#qte_input').val(cste_local);
        $('#qte_input').trigger('input');
        cste_init = cste_plein;
    },
});

    // Changement de l'icone consigne suivant la valeur de qte_input

function ChangeIcone(x){
    var cste_local = $('.consigne_column[id_consigne='+ x +']');
    if(cste_local.hasClass('consigne_active')){
    }
    else{
        var val = $('.consigne_active').children('.consigne_image').attr('data_vide');
        $('.consigne_active').removeClass("consigne_active").children('.consigne_image').attr('src', val);
        cste_local.addClass("consigne_active");
        val = cste_local.children('.consigne_image').attr('data_plein');
        cste_local.children('.consigne_image').attr('src', val);
    }
}

/* Fin changement d'image du bocal en survole */

/* début changement de consigne suivant la quantité qte_input choisie */

function IdConsigne(x){
    //console.log(tab_consigne.length);
    for(var key in tab_consigne){
        //console.log(key);
        //console.log(tab_consigne[key]);

        if(x <= tab_consigne[key]){
            //console.log(key);
            //console.log(tab_consigne[key]);
            return key;
        }
    }
}

/* Fin changement de consigne suivant la quantité qte_input choisie */

/* début mise à jour du prix qte_input */

$('#qte_input').on({
  input: function()
    {
      // changement des images bocal consigné

      var val_qte = parseFloat($(this).val().replace(",", ".")); // quantité précise saisie

      // Vérification de la valeur dans input
      if(isNaN(val_qte) || val_qte <= 0){
        // $('#error_qte').show(200);
        //$('#prix_cal').text('-');
        $('#prix_cal').text('0,00');
        $('.emballage_div').hide();
        ChangeIcone(0);
        return false;
      }
      else if(val_qte > qte_max){
        val_qte = qte_max;
        $('#qte_input').val(val_qte);
      }

      // Mise à jour du prix total

      var calc = parseFloat(val_qte * prix_article).toFixed(2);
      $('#prix_cal').text(calc.replace(".", ","));

      // Correspondance entre la valeur qte_input et la consigne concernée

      if(cons_kraft == 1){
        var local_id = IdConsigne(val_qte);
        var local_prix;
        ChangeIcone(local_id);
        local_prix = $('.consigne_column[id_consigne='+ local_id +']').attr('data_prix_consigne');
        $('#affiche_prix_emballage').text(local_prix);
        $('.emballage_div').show();
      }
      else{
        $('.emballage_div').hide();
        $('#affiche_prix_emballage').text('-');
      }
    }
  });

/* Début choix entre Consigne ou Kraft*/

    // afficher l'option Kraft pour l'emballage

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

        cons_kraft = 2; // option 2: Kraft choisie - Initialisation au début

        $('#qte_input').trigger("input"); // adapter le prix de l'emballage kraft lors de la selection en kraft
      }
    });


        // Retour à l'option Consigne

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

        cons_kraft = 1;// option 1: Consigne choisie - Initialisation au début
        $('#qte_input').trigger("input"); // adapter la taille du local suivant la valeur choisie pendant la position de l'onglet en kraft
      }
    });

/* Fin choix entre Consigne ou Kraft*/

/* Début choix entre Description ou Producteur*/

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

/* Fin choix entre Description ou Producteur*/


/*
//data_panier['data_produit']= $(".data_produit").val();
//data_panier['data_consigne']= $(".data_consigne").val();

console.log(JSON.stringify(data_panier));
var link = $('.form_achat_produit').serialize();
var data_produit = $(".data_produit").val();
	var data_consigne = $(".data_consigne").val();
*/
console.log(window.location.href);
/* Début Pop up add_rapid : création de l'ajax pour ajouter au panier */
	$('.ajout_panier').on({
	click: function(){
	//var link = $('.form_achat_produit').serialize();
	//var data_panier = {};
	var data_panier = {
        data_produit: $(this).attr('data_produit'),
        data_consigne: cons_kraft,
        qte_input: $("#qte_input").val(),
        nb_article: $('#nbr_article_dans_panier').text(),
    };
	//console.log(data_panier);

	$.ajax({
	    type: 'POST',
	    url: '/boutique/panier',
	    data: data_panier,/*{
	        'data_produit': data_produit,
	        'data_consigne': data_consigne,
	        'qte_input': qte_input,
	        },*/

	        success: function(data) {
	        // if there are still more pages to load,
	        // add 1 to the "Load More Posts" link's page data attribute
	        // else hide the link
	        /*if (data.has_next) {
	            link.data('page', page+1);
	            } else {
	            link.hide();
	            }*/
	        $('.bordure_bas').append('data : ' + data.sessionqte + '   data2: ' + data.nb_article);
	        $('#nbr_article_dans_panier').text(data.nb_article);
	        if(data.same){
	            var cste = $('.ajout_panier').attr('data_produit');
	            $('.ajax_nb_' + cste + '').text(data.nb_qte);
	            // console.log(data.nb_qte);
	            // $('.consigne_column[id_consigne='+ local_id +']').attr('data_prix_consigne');
	            }
	        else{
	            $('.panier_vide_msg').hide();
                $('.ajout_dans_panier').prepend('<div class="classArticlePanier"' + $('.ajout_panier').attr('data_produit') + '"><img src="' + $('.image_produit').attr('src') + '"><div class="panier_milieu"><p class="panier_titre"><a href="' + window.location.pathname + '">' + $('.titre_article').text() + '</a><span> - ' + $('.prix_produit').text() + '</span></p><p class="panier_sousTitre">Poids (g) : <span>' + data.val_qte + '</span></p><p class="panier_sousTitre">Consigne comprise : <span>' + $('#affiche_prix_emballage').text() + '</span></p></div><div class="panier_prixArticle"><p><span>x </span><span class="ajax_nb_' + $('.ajout_panier').attr('data_produit') + '">' + data.nb_qte + '</span></p><p>' + $('#prix_cal').text() + '€</p></div></div>');
                }
	        },

	        error: function(xhr, status, error) {
	            // shit happens friends!
	        }
	    });
	}
	});

/* Fin Pop up add_rapid : création de l'ajax pour ajouter au panier */

/* Début Gestion des cookies */
/*
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
      var data_img = $('.image_produit').attr('src');
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
          $('#'+ id).html('<div class="classArticlePanier"><img src="' + v.data_img + '"><div class="panier_milieu"><p class="panier_titre"><a href="' + v.url + '">' + v.nom + '</a><span> - ' + v.typ_pri + '</span></p><p class="panier_sousTitre">Poids (g) : <span>' + v.val_qte + '</span></p><p class="panier_sousTitre">Consigne comprise : <span>' + v.info_prix_emballage + '</span></p></div><div class="panier_prixArticle"><p><span>x </span>' + v.qt + '</p><p>' + v.prix_tot + '</p></div></div>');
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
          data_img: data_img,
          url: url
        });
        $('.ajout_dans_panier').prepend('<div class="classArticlePanier"><img src="' + data_img + '"><div class="panier_milieu"><p class="panier_titre"><a href="' + url + '">' + nom + '</a><span> - ' + typ_pri + '</span></p><p class="panier_sousTitre">Poids (g) : <span>' + val_qte + '</span></p><p class="panier_sousTitre">Consigne comprise : <span>' + info_prix_emballage + '</span></p></div><div class="panier_prixArticle"><p><span>x </span>' + qt + '</p><p>' + prix_tot + '</p></div></div>');
      }

      // sauvegarde le panier -> fonction dans le fichier base_fonctions.js
      save_panier(nbrArticleDansPanier, articlesPanier);

      // affiche le contenu du panier si c'est le premier article -> fonction dans le fichier base_fonctions.js
      panier_vide_toggle();
    });
*/
/* Fin Gestion des cookies */

});
//fin