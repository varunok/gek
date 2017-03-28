/**
 * Created by varunok on 28.03.17.
 */
$(document).ready(function() {
    $('.menu_wrap').on('click', 'li', function (event) {
        event.preventDefault();
        $('.menu_wrap a').removeClass('active');
        $(this).children('a').addClass('active');
        var section = $(this).children('input').val();
        $.get('', {'section': section})
                .then(function(response) {
                    $('#add-section').html(response)
                }, function(err) {});
    })
});