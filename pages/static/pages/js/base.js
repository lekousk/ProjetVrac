
// Attente du chargement entier du DOM

$(function() {
	//document.onload = function() {

	/* JS */

	// Affichage du menu avec le Burger button pour media < 900 px

	$('#nav_bt_burger').on('click', function(){
		$('.bandeau_fond').slideToggle('slow');
		$('div.bloc_principaux').toggleClass("nav_open");
		$('.sousMenu').hide('slow');
	});

	// Affichage du menu pour un pointer coarse (tactile) et/ou une petite taille

	function menu_tac_petit(){
		var taille_p = window.matchMedia("(max-width: 900px)").matches;
		var is_coarse = matchMedia('(pointer:coarse)').matches;

		if(is_coarse || taille_p)
		{
			$('.menu_a').on("click", function(){
				return false;
			});

			$('.menu_a').on('click', function(){
				var nextAZ = $(this).next();
				if(nextAZ.hasClass('sousMenu'))
				{
					nextAZ.slideToggle('slow');
				}
			});
		}
	}

	menu_tac_petit();

	// Gestion en cas de redimensionnement de la fenêtre

	$(window).resize(function() {
		menu_tac_petit();
		menu_resize();
		even_taille();
	});

	// Annule les effets du bouton Burger si utilisation en taille petite
	
	function menu_resize(){
		if($('div.bloc_principaux').hasClass("nav_open")){
			$('#nav_bt_burger').trigger('click');
		}
	}

	// Gestion des évènements quand le pointer est coarse (tactile) ET la taille de l'écran petite

	function even_taille(){
		var is_coarse = matchMedia('(pointer:coarse)').matches;
		var taille_p = window.matchMedia("(max-width: 900px)").matches;

		if(is_coarse && taille_p){
			$('.panier').on('click', function(){
				$('.panier_reduit').slideToggle('slow');
				$(".basket").toggleClass("active");
			});

			// Click hors des éléments, avec pointer coarse, gestion des évènements :
			$(document).on("click", function(e){
				var horsBasket = !$(e.target).closest('.basket').length;
				var actBasket = $('.basket').hasClass("active");
				if(horsBasket && actBasket){
					$('.panier').trigger("click");
				}
			});
		}
		// Gestion des évènements hors tactile ET petit écran
		else{

			// comportement du panier au survol pour affichage de son contenu
			var timeout;
			$('.panier').on({
				mouseenter: function(){
					$('.panier_reduit').show();
				},
				mouseleave: function(){
					timeout = setTimeout(function(){
						$('.panier_reduit').hide();
					}, 300);
				}
			});

			// laisse le contenu ouvert à son survol
			// le cache quand la souris sort

			$('.panier_reduit').on({
				mouseenter: function(){
					clearTimeout(timeout);
				},
				mouseleave: function(){
					$('.panier_reduit').hide();
				}
			});

			// Scroll up + A mettre dans la partie media queries > 1030px
			$(window).scroll(function (){
				if ($(this).scrollTop() > 180 ) {
					$('#scrollUp').show('slow');
				}
				else {
					$('#scrollUp').hide( 'slow' );
				}
			});
		}
	}

	even_taille();


	/*$('.header_nav').on('mouseenter', function(){
		var n_href;
		if(false)
		{
		$('.navigation a').each(function(i){
			console.log(i + ':' + $(this).attr('_href'));
			n_href = $(this).attr('_href');

			if (n_href)
			{
				$(this).attr('href', n_href);
			}
		});
		}
	});*/


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
