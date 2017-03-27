(function ($) {
	$(document).ready(function() {
		$("#expanded_btn").click(function() {
			$(this).parents('.footer').toggleClass('active');
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
			asNavFor: '#slider_nav',
				responsive: [
				    {
				      breakpoint: 768,
				      settings: {
				        adaptiveHeigth: true
				      }
				    }
			  	]
		});
		$('#slider_nav').slick({
			slidesToShow: 6,
			slidesToScroll: 1,
			asNavFor: '#slider_for',
			focusOnSelect: true,
				responsive: [
				    {
				      breakpoint: 768,
				      settings: {
				        slidesToShow: 2,
				        slidesToScroll: 1
				      }
				    }
			  	]
		});
		$('.block_newbuilding_row .field_image').slick({
			slidesToShow: 1,
			slidesToScroll: 1,
			adaptiveHeigth: true
		});
		$('#slider_video').slick({
			slidesToShow: 2,
			slidesToScroll: 1,
			responsive: [
			    {
			      breakpoint: 768,
			      settings: {
			        slidesToShow: 1,
			        slidesToScroll: 1,
			        arrows: false,
			        dots: true
			      }
			    }
		  	]
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
		$('#block-webform .close, #block-webform-confirm .close, .popup_exit').livequery('click', function(){
			$('#block-webform, .popup_exit, #block-webform-confirm').fadeOut();
			$('body').removeClass('popup');
		});
		$('.to_up').livequery('click', function () {
			$('body, html').scrollTo('.header', 1500);
		})
		if ($(window).width() > 768) {			
			$('.reviews_text').masonry({
			  // options
			  itemSelector: '.view_row',
			  gutter: 30
			});
		}
		$('.star, .icons_wrap .icon.favorite').livequery('click', function () {
			$(this).toggleClass('active');
		})
		$('.block_seo .read_more a').livequery('click', function () {
			$(this).parents('.block_seo').addClass('active');
			return false;
		})
		$('.apartment .slider_main .webform_client_form .form-submit').livequery('click', function () {
			$('#block-webform, .popup_exit').fadeIn();
		})

		if ($(window).width() < 768) {
			$('.block_main_menu').slicknav({
				label:'',
				prependTo: '.header_content .contacts_header'
			});
			$('.block_articles .read_more').insertAfter('.block_articles .view_content');
			$('.block_shops:not(.block_newbuilding_row) .view_content, .new_buildings .view_content, .block_articles .view_content_inner, .block_should_use .view_content, .block_photo .view_content, body:not(.repair_premises):not(.trust):not(.installation_water):not(.plan):not(.property_valuation):not(.superlending) .block_benefits:not(.steps) .view_content, .repair_premises .block_our_works .view_content, .block_diplomas .view_content, .trust .block_vip_shops .view_content, .earth .block_vip_shops .view_content, .apartment .block_vip_shops .view_content, .contacts .block_vip_shops .view_content').slick({
				slidesToShow: 1,
				slidesToScroll: 1,
			    arrows: false,
			    dots: true
			});
			$('.front .block_articles .view_content').slick({
				slidesToShow: 1,
				slidesToScroll: 1,
			    arrows: false,
			    dots: true
			});
			$('.block_reviews .reviews_text').slick({
				slidesToShow: 1,
				slidesToScroll: 1,
			    arrows: false,
			    dots: true,
			    adaptiveHeigth: true
			});
			$('.footer_right .contacts_header').appendTo('.footer_right');
			$('.footer_right').insertAfter('.footer .logo');
			$('.footer_center').insertAfter('.footer_right');
			$('.block_process .block_content .views_row .left_wrap').livequery(function(){
				$(this).insertAfter($(this).next('.right_wrap'));				
			})
			$('.block_tests_wrapper .views_row .right_wrap').livequery(function(){
				$(this).prependTo($(this).parents('.view_row_inner'));				
			})
			$('.block_tests_wrapper .views_row .left_wrap .read_more').livequery(function(){
				$(this).appendTo($(this).parents('.view_row_inner'));				
			})
			$('.block_process .block_content .views_row .right_wrap .webform_client_form .form_textarea').livequery(function(){
				$(this).insertAfter($(this).next('.group'));				
			})
			$('.process .left_sidebar .banner').insertAfter('.block_presentation');

			$('.block_services_wrap .views_row.odd .right_wrap').livequery(function(){
				$(this).prependTo($(this).parents('.views_inner'));				
			})
			$('.block_vip_shops .views_row .views_body, .block_shops.block_search_results .views_row .views_body').livequery(function(){
				$(this).find('.statistics').appendTo($(this).find('.top_wrap'));				
				$(this).find('.price.info').prependTo($(this).find('.bottom_wrap'));				
			})
			$('.new_buildings .views_row .statistics').livequery(function(){
				$(this).insertAfter($(this).parents('.views_body').find('.address'));			
			})
			$('.new_buildings .views_row .price').livequery(function(){
				$(this).insertAfter($(this).parents('.views_body').find('.read_more'));			
			})
			$('.ranking .left_sidebar .property_search').prependTo('.middle_inner');

		}

	});
})(jQuery);