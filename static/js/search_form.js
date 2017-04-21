/**
 * Created by varunok on 10.04.17.
 */
$(document).ready(function() {
    $('.left_sidebar').on('click', '.searh-form', function (event) {
        event.preventDefault();
        var data = $('.search-form').serialize();
        var action = $('.search-form').attr('action')
        $.post(action, data)
            .then(function(response) {
                var data = $.parseJSON(response);
                $('.list-building').html(data.html);
                }, function(err) {});
    })
});