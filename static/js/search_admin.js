/**
 * Created by varunok on 07.06.17.
 */
$(document).ready(function() {
    $('.search-admin').on('click', function (event) {
        event.preventDefault();
        var sf = $('.search-form');
        if(sf.hasClass('active')){
            sf.removeClass('active').fadeOut();
        }else{
            sf.addClass('active').fadeIn();
        }
    })
});