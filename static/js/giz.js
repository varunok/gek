(function ($) {
	$(document).ready(function() {
		$("#expanded_btn").click(function() {
			$(this).next('.disabled').slideToggle();
			return false;
		});
		$('.slider').slick({
			slidesToShow: 1,
			slidesToScroll: 1
		});
		$( ".form_item.date input" ).datepicker({
			dateFormat: "dd MM yy"
		});
		
		$('#slider_for').slick({
			slidesToShow: 1,
			slidesToScroll: 1,
			arrows: false,
			fade: true,
			arrows: true,
			asNavFor: '#slider_nav'
		});
		$('#slider_nav').slick({
			slidesToShow: 6,
			slidesToScroll: 1,
			asNavFor: '#slider_for',
			focusOnSelect: true
		});
		$('.block_newbuilding_row .field_image').slick({
			slidesToShow: 1,
			slidesToScroll: 1,
			adaptiveHeigth: true
		});
		$('#slider_video').slick({
			slidesToShow: 2,
			slidesToScroll: 1
		});
		$('.block_questions .views_row').livequery('click', function () {
			$(this).toggleClass('active');
		})
		$('#block-webform').livequery(function(){
			var hei = $(this).innerHeight();
			hei = hei / 2;
			hei = '-'+hei+'px';		
			$(this).css('margin-top', hei);	
		});
		$('#block-webform .close').livequery('click', function(){
			$('#block-webform').fadeOut();
			$('body').removeClass('popup');
		});
		$('.to_up').livequery('click', function () {
			$('body, html').scrollTo('.header', 1500);
		})
		$('.reviews_text').masonry({
		  // options
		  itemSelector: '.view_row',
		  gutter: 30
		});

	});
})(jQuery);