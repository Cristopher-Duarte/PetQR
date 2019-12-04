var $;



$(document).ready(go);
var contador = 1;

function go () {
$('.bt-menu').click(function(){
    if (contador == 1) {
        $('nav').animate({
            left: '0'
        });
        contador = 0;
    } else {
        contador = 1;
        $('nav').animate({
            left: '-100%'
        });
    }
});
} 