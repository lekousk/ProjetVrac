
// Attente du chargement entier du DOM

$(function() {
	//document.onload = function() {

	/* JS */

	// Affichage du menu avec le Burger button pour media < 900 px

	$('#nav_bt_burger').on('click', function(){
		$('.bf_mobile').slideToggle('slow');
		$('div.bloc_principaux').toggleClass("nav_open");
		$('.sousMenuMob').hide('slow');
		$('html').toggleClass("supprScroll");
	});

	// Affichage du menu pour un pointer coarse (tactile) et/ou une petite taille

	var taille_p;
	var is_coarse;

	function menu_tac_petit(){
		taille_p = window.matchMedia("(max-width: 900px)").matches;
		is_coarse = matchMedia('(pointer:coarse)').matches;
	}

	menu_tac_petit();

	function suppr_href() {
		$('.menu_a').each(function(i) {
			var data_href;
			if($(this).next().hasClass("sousMenuMob") && $(this).attr("href"))
			{
				data_href = $(this).attr("href");
				$(this).attr("data_href", data_href);
				$(this).removeAttr("href");
			}
		});
	}

	function use_dataHref() {
		$('.menu_a').each(function(i) {
			var data_href;
			if($(this).attr("data_href") && !$(this).attr("href"))
			{
				data_href = $(this).attr("data_href");
				$(this).attr("href", data_href);
			}
		});
	}

	// Affichage des menus avec media > 901px au survol

	$('li.affnav').hover(function(){
	    var affmenu = $(this).children(".sousMenu");
		if(!is_coarse && !taille_p)
		{
			if(affmenu)
			{
				affmenu.slideDown('fast');
			}
		}
	}, function(){
	    var affmenu = $(this).children(".sousMenu");
		if(!is_coarse && !taille_p)
		{
			affmenu.hide();
		}
	});

	// Affichage des menus si media < 900px et pointer coarse

	$('.menu_a').on('click', function(){
		if(is_coarse || taille_p)
		{
			var nextAZ = $(this).closest("li").children("ul");
			if(nextAZ.hasClass("sousMenuMob"))
			{
				nextAZ.slideToggle('slow');
			}
		}
	});

	// Au démarrage, si écran petit ou pointeur coarse (tactile)
	
	if(taille_p || (taille_p && is_coarse))
	{
		suppr_href();
		voirTout();
	}
	// Au démarrage, pointeur coarse (tactile) et grand écran
	else if(is_coarse)
	{
		// Ajout de la propriété flex en JS car css, la class n'accepte pas display: flex et none
		$('.subMenu1').css("display", "flex");
		$('.subMenuP').hide();
		suppr_href();
		voirTout();
	}
	// Au démarrage, Grand écran, peut importe le pointer
	else
	{
		// Ajout de la propriété flex en JS car css, la class n'accepte pas display: flex et none
		$('.subMenu1').css("display", "flex");
		$('.subMenuP').hide();
	}

	// Fonction pour le démarrage, insertion de "Voir tout" pour le pointeur coarse et/ou petit écran
	
	function voirTout(){
		var lien_vt;
		$('.voir_tout').each(function(){
			lien_vt = $(this).attr("href");
			$(this).next("ul.sousMenu").prepend('<li><a class="menu_3" href="' + lien_vt + '">Voir tout</a></li>');
		});
	}

	// Gestion en cas de redimensionnement de la fenêtre

	var rtime;
	var timeout = false;
	var delta = 200;

	$(window).on('resize', function() {

		ind_resize = true;
		rtime = Date.now();
		if(timeout === false)
		{
			timeout = true;
			setTimeout(resizeFenetre, delta);
		}
	});

	function resizeFenetre() {

		if(Date.now() - rtime < delta) {
			setTimeout(resizeFenetre, delta);
		}
		else {
			timeout = false;
			menu_tac_petit();
			menu_resize();
			if(is_coarse || taille_p)
			{
				suppr_href();
			} else {
				use_dataHref();
			}
			if($('.fTrier').hasClass('activeFtrier') && !taille_p)
			{
				$('.margeTr').trigger('click');
				$('.partRayon').show('slow');
				$('.partTrier').show('slow');
			}
		}
	}

	// Annule les effets du bouton Burger si utilisation en taille petite

	function menu_resize(){
		console.log('menu_resize');
		if(taille_p)
		{
			if($('div.bloc_principaux').hasClass("nav_open")){
				$('#nav_bt_burger').trigger("click");
			}
			$('.bandeau_fond').hide();
			$('.sousMenuMob').hide();
			$('.subMenu1').css("display", "");  // Suppression de la propiété display: flex
		}
		else{
			$('.bandeau_fond').slideDown();
			$('.subMenu1').css("display", "flex");
			$('.sousMenu').hide();
			$('.subMenu2').show();
		}
	}

	// Gestion des évènements quand le pointer est coarse (tactile) ET la taille de l'écran petite


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
		var timepanier;
		$('.panier').on({
			mouseenter: function(){
				$('.panier_reduit').show();
			},
			mouseleave: function(){
				timepanier = setTimeout(function(){
					$('.panier_reduit').hide();
				}, 300);
			}
		});

		// laisse le contenu ouvert à son survol
		// le cache quand la souris sort

		$('.panier_reduit').on({
			mouseenter: function(){
				clearTimeout(timepanier);
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

/*
	// Récupérer les informations dans les cookies

	nbrArticleDansPanier = parseInt(getCookie('nbrArticleDansPanier') ? getCookie('nbrArticleDansPanier') : 0);
	articlesPanier = getCookie('articlesPanier') ? JSON.parse(getCookie('articlesPanier')) : [];

	panier_vide_toggle();  // A activer !!!!!

	// Afficher le nombre d'article du panier dans le widget

	$('#nbr_article_dans_panier').html(nbrArticleDansPanier);

	// Articles trouvés dans le cookie
	articlesPanier.forEach(function(v) {
		items += '<div class="classArticlePanier"><img src="' + v.data_img + '"><div class="panier_milieu"><p class="panier_titre"><a href="' + v.url + '">' + v.nom + '</a><span> - ' + v.typ_pri + '</span></p><p class="panier_sousTitre">Poids (g) : <span>' + v.val_qte + '</span></p><p class="panier_sousTitre">Consigne comprise : <span>' + v.info_prix_emballage + '</span></p></div><div class="panier_prixArticle"><p><span>x </span>' + v.qt + '</p><p>' + v.prix_tot + '</p></div></div>';
	});

	// Ajout des items dans le panier ul
	$('.ajout_dans_panier').prepend(items);
*/
});
//fin
