//Attente chargement du DOM

$(function() {

$('.chmdp').on('click', function(){
    $('.chmdpform').slideToggle('slow');
    $(this).children().toggleClass('arrowTarget');
});

$('.supprcmt').on('click', function(){
    $('.affsupprcmt').slideToggle('slow');
    $(this).children().toggleClass('arrowTarget');
});

});