var $;
$(document).ready(go);
var contador = 1;

function go () {
$('.TAP').click(function(){
    if (contador == 1) {
        $('nav').animate({
            left: '0'
        })  
    }})
};
window.onload = function esconder(){
    $('nav').animate({
        left: '-100%'
    }); 
};