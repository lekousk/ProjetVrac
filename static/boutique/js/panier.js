// Attente du chargement entier du DOM

$(function() {

// afficher l'option Kraft pour l'emballage

$('#li_kraft').on({
  click: function() {
    $('#consigne_table').hide(200).queue(function(){
      $('#zone_kraft').show(200);
      $(this).dequeue();
    });
    $('#li_cons').animate({'border-bottom-width': '0px', 'opacity': '0.6'}, 100);
    $(this).animate({'border-bottom-width': "3px", 'opacity': '1'}, 100);
    $(this).off("mouseenter mouseleave"); // annuler le hover sur le passage de Kraft. 2e solution ? ($(this).unbind('mouseout mouseover')();)
    $("#li_cons").hover(function(){
      $(this).css("opacity", "1");
      }, 
      function(){
      $(this).css("opacity", "0.6");
      }
    );
  }
});



// Revenir à l'option Consigne pour l'emballage

$('#li_cons').on({
  click: function() {
    $('#zone_kraft').hide(200).queue(function()
      {
        $('#consigne_table').show(200);
        $(this).dequeue();
      }
    );
    $('#li_kraft').animate({'border-bottom-width': '0px', 'opacity': '0.6'}, 100);
    $(this).animate({'border-bottom-width': "3px", 'opacity': '1'}, 100);
    $(this).off("mouseenter mouseleave");
    $("#li_kraft").hover(function()
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

// Afficher la description du producteur



$('#li_prod').on({
  click: function() {
    $('#art_desc').hide(200).queue(function()
      {
        $('#art_prod').show(200);
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
    $('#art_prod').hide(200).queue(function()
      {
        $('#art_desc').show(200);
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

// Survole des titres pour l'emballage et la description dans toutes les situations

var select_img_s = 0;

var etat_img_s = 0;

var val_s_max = parseInt($('#val_s_max').text()); // quantité de la valeur pleine du contenant S

var val_m_max = parseInt($('#val_m_max').text()); // quantité de la valeur pleine du contenant M

var val_l_max = parseInt($('#val_l_max').text()); // quantité de la valeur pleine du contenant L

var val_xl_max = parseInt($('#val_xl_max').text()); // quantité de la valeur pleine du contenant XL

/*$('#img_s').on({
  mouseenter: function() 
    {
    $('#img_s').attr({'src': "/static/boutique/images/leBocalTampon_couleur.png"});
    },
  mouseleave: function() 
    {
    $('#img_s').attr({'src': "/static/boutique/images/leBocalTampon.png"});
    }
});*/

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
      var val_qte = parseInt($('#qte_input').val()); // quantité précise saisie
      change_qte(val_qte, val_s_max, val_m_max, val_l_max, val_xl_max);
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
  }

  else if ( 0 < val_qte && val_qte <= val_s_max) 
  {
    $('#img_s').attr({'src': "/static/boutique/images/leBocalTampon_plein.png"});
    $('#img_m').attr({'src': "/static/boutique/images/leBocalTampon.png"});
    $('#img_l').attr({'src': "/static/boutique/images/leBocalTampon.png"});
    $('#img_xl').attr({'src': "/static/boutique/images/leBocalTampon.png"});
  }

  else if (val_s_max < val_qte && val_qte <= val_m_max) 
  {
    $('#img_m').attr({'src': "/static/boutique/images/leBocalTampon_plein.png"});
    $('#img_s').attr({'src': "/static/boutique/images/leBocalTampon.png"});
    $('#img_l').attr({'src': "/static/boutique/images/leBocalTampon.png"});
    $('#img_xl').attr({'src': "/static/boutique/images/leBocalTampon.png"});
  }

  else if (val_m_max < val_qte && val_qte <= val_l_max)
  {
    $('#img_l').attr({'src': "/static/boutique/images/leBocalTampon_plein.png"});
    $('#img_s').attr({'src': "/static/boutique/images/leBocalTampon.png"});
    $('#img_m').attr({'src': "/static/boutique/images/leBocalTampon.png"});
    $('#img_xl').attr({'src': "/static/boutique/images/leBocalTampon.png"});
  }

  else if (val_l_max < val_qte && val_qte <= val_xl_max) 
  {
    $('#img_xl').attr({'src': "/static/boutique/images/leBocalTampon_plein.png"});
    $('#img_s').attr({'src': "/static/boutique/images/leBocalTampon.png"});
    $('#img_m').attr({'src': "/static/boutique/images/leBocalTampon.png"});
    $('#img_l').attr({'src': "/static/boutique/images/leBocalTampon.png"});
  }

  else
  {
    $('#error_qte').show(200);
    $('#img_s').attr({'src': "/static/boutique/images/leBocalTampon.png"});
    $('#img_m').attr({'src': "/static/boutique/images/leBocalTampon.png"});
    $('#img_l').attr({'src': "/static/boutique/images/leBocalTampon.png"});
    $('#img_xl').attr({'src': "/static/boutique/images/leBocalTampon.png"});
  }
}




});
//fin