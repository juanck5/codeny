$(document).ready(function(){
    console.log("ANDANDO");
	var altura = $('.navegador').offset().top;
	
	$(window).on('scroll', function(){
		if ( $(window).scrollTop() > altura ){
			$('nav').addClass('menu-fixed');
		} else {
			$('nav').removeClass('menu-fixed');
		}
	});

});