//Attente chargement du DOM

$(function() {
	// Code ci-dessous
	//
	// Affichage, choix entre liste ou mosaique
	var cookieAff = true;
	var prefAff;
	$('.mosaic_list').on('click', function(){
		$(this).parent().toggleClass("list_square");
		$(".resultat_recherche").toggleClass("list").toggleClass("mosaic");
		// Enregistrement choix d'affichage (liste ou mosaic) dans un cookie
		if ($(".resultat_recherche").hasClass("list")){
			setCookie("prefAff", "list");
		}
		else{
			setCookie("prefAff", "mosaic");
		}
	});

	// Affichage (liste ou mosaic) lors du chargement de la page, si cookie
	if (cookieAff) {
		prefAff = getCookie("prefAff");
		if(prefAff == "mosaic"){
			$(".mosaic_list").trigger("click");
		}
		cookieAff = false;
	}

	//
	//affichage de la partie "Trier"
	
	var TrOuRay = false;

	$('.trier').on('click', function(){
		$('.partRayon').hide();
		$('.partTrier').show();
		$('.fTrier').toggleClass("activeFtrier");
		$('html').toggleClass("supprScroll");
	});

	$('.rayons').on('click', function(){
		$('.partRayon').show();
		$('.partTrier').hide();
		$('.fTrier').toggleClass("activeFtrier");
		$('html').toggleClass("supprScroll");
		TrOuRay = true;
	});

	$('.margeTr').on('click', function(){
		$('.fTrier').toggleClass("activeFtrier");
		$('html').toggleClass("supprScroll");
		$('.partRayon').delay(400).slideDown();
		$('.partTrier').delay(400).slideDown();
		clearFTrier();
		TrOuRay = false;
	});

	$('.btnCroix').on('click', function(){
		$('.margeTr').trigger('click');
	});

	// Effacement des filtres dans la barre du récapitulatif des filtres
	$('.btnCroixEff').on('click', function(){
		$('.btnEff').trigger('click');
	});

	var valRecap;

	$('.searchEach').on('click', function(){
		valRecap = $(this).attr('data-fi');
		if(valRecap){
			posRecap = fiTab.indexOf(valRecap);
			fiTab.splice(posRecap, 1);
			$('.InputFi').attr('value', fiTab);
		}else{
			valRecap = $(this).attr('data-ray');
			posRecap = rayTab.indexOf(valRecap);
			rayTab.splice(posRecap, 1);
			$('.InputRay').attr('value', rayTab);
		}
		$('.btnInputRayTr').trigger('click');
	});

	//
	//Selection d'un rayon après une recherche et insertion dans l'input dédié
	// Création d'une liste comprenant tous les id des catégories choisies
	var rayTab = [], initRay =[];
	var fiTab = [], initFi = [];
	var valTr, initTr;
	var idTab, valTab;

	$('.ficat').on('click', function(){
		valTab = $(this).attr('data-ray');
		idTab = rayTab.indexOf(valTab);
		if(idTab >= 0){
			rayTab.splice(idTab,1);
		}
		else{
			rayTab.push(valTab);
		}
		$(this).toggleClass("checkOk");
		console.log(rayTab);
		console.log('val: ' + valTab);
		console.log('id: ' + idTab);
		$('.InputRay').attr('value', rayTab);
	});
	$('.fiprod').on('click', function(){
		valTab = $(this).attr('data-fi');
		idTab = fiTab.indexOf(valTab);
		if(idTab >= 0){
			fiTab.splice(idTab,1);
		}
		else{
			fiTab.push(valTab);
		}
		$(this).toggleClass("checkOk");
		console.log(fiTab);
		console.log('val: ' + valTab);
		console.log('id: ' + idTab);
		$('.InputFi').attr('value', fiTab);
	});

	$('.fitri').on('click', function(){
		valTab = $(this).attr('data-tr');
		if(valTr == valTab){
		}
		else{
			$(this).toggleClass("checkOk");
			$('.fitri').each(function(){
				idTab = $(this).attr('data-tr');
				if(valTr == idTab){
					$(this).toggleClass("checkOk");
					return false;
				}
			});
			$('.InputTr').attr('value', valTab);
			valTr = valTab;
		}
		console.log('val: ' + valTr);
		console.log('id: ' + idTab);
	});

	function RayInit(){
		var rayTab = [];
		var temp;
		temp = $('.InputRay').attr('value');
		if(temp){
			rayTab = $('.InputRay').attr('value').split(',');
		}
		for(var a = 0; a < rayTab.length; a++){
			$('.ficat').each(function(){
				if($(this).attr('data-ray') == rayTab[a]){
					$(this).toggleClass("checkOk");
				}
			});
		}
		return rayTab;
	}

	function FiltreInit(){
		var fiTab = [];
		var temp;
		temp = $('.InputFi').attr('value');
		if(temp){
			fiTab = $('.InputFi').attr('value').split(',');
		}
		for(var a = 0; a < fiTab.length; a++){
			$('.fiprod').each(function(){
				if($(this).attr('data-fi') == fiTab[a]){
					$(this).toggleClass("checkOk");
				}
			});
		}
		return fiTab;
	}

	function TrierInit(){
		var valTr;
		var temp;
		valTr = $('.InputTr').attr('value');
		if(valTr){
			$('.fitri').each(function(){
				temp = $(this).attr('data-tr');
				if(valTr == temp){
					$(this).toggleClass("checkOk");
					return false;
				}
			});
		}
		else{
			$('.pertinence').toggleClass("checkOk");
			valTr = 1;
		}
		return valTr;
	}

	// Initialisation des filtres et tri
	rayTab = RayInit();
	fiTab = FiltreInit();
	valTr = TrierInit();

	// Stockage des valeurs initiales
	initRay = $('.InputRay').attr('value');
	initFi = $('.InputFi').attr('value');
	initTr = $('.InputTr').attr('value');

	//Effacer la  sélection des filtres
	$('.btnEff').on('click', function(){
		$('.InputRay').attr('value', '');
		$('.InputFi').attr('value', '');
		$('.InputTr').attr('value', '');
		$('.btnInputRayTr').trigger('click');
	});

	function clearFTrier(){
		$('.checkboxFi').each(function(){
			if($(this).hasClass('checkOk')){
				$(this).removeClass("checkOk");
			}
		});
		$('.InputRay').attr('value', initRay);
		$('.InputFi').attr('value', initFi);
		$('.InputTr').attr('value', initTr);
		rayTab = RayInit();
		fiTab = FiltreInit();
		valTr = TrierInit();
	}

	//Validation des filtres / Tris est des Rayons
	//La validation des rayons annulent les filtres / tris
	$('.btnInputDep').on('click', function(){
		/*if(TrOuRay){
			$('.InputFi').remove();
			$('.InputTr').remove();
		}*/
		$('.btnInputRayTr').trigger('click');
	});

	// Affichage grand format > 901px
	// Gestion de trier
	var horsTrier = false;
	$('.voletTrier:first').on('click', function(){
		$('.trierMin').slideToggle();
		$('.arrowTrier').toggleClass('arrowTarget');
		if(horsTrier){
			horsTrier = false;
		} else{
			horsTrier = true;
		}
	});

	$(document).on("click", function(e){
		if(horsTrier && !$(e.target).closest('.voletTrier').length){
			$('.voletTrier:first').trigger('click');
		}
	});

});
//Fin
