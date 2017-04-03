/**
 * Created by varunok on 31.03.17.
 */
$(document).ready(function() {
    $('.serviceStatus').on('change', 'input[type=checkbox]', function () {
        var data = $(this).parents('.slideThreeForm').serialize();
        $.post('status_service', data)
                .then(function(response) {
                    notify_success(response, 'Успешно');
                }, function(err) {
                    notify_error('Ошибка '+ err.status, err.statusText);
                });
    });

    $('.faqStatus').on('change', 'input[type=checkbox]', function () {
        var data = $(this).parents('.statusFaqForm').serialize();
        $.post('status_faq', data)
                .then(function(response) {
                    notify_success(response, 'Успешно');
                }, function(err) {
                    notify_error('Ошибка '+ err.status, err.statusText);
                });
    });
    $('#delete-image').click(function (event) {
        event.preventDefault();
        var content_type = $(this).next().val();
        _this = $(this);
        $.get('delete-image', {'content_type': content_type})
            .then(function(response) {
                    notify_success(response, 'Успешно');
                    $('#blah').attr("src","second.jpg");
                    _this.fadeOut();
                }, function(err) {
                    notify_error('Ошибка '+ err.status, err.statusText);
                });
    })

});