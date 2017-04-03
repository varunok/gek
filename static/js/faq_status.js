/**
 * Created by varunok on 02.04.17.
 */
$(document).ready(function() {
    $('.faqForm').on('click', '#create_faq', function (event) {
        event.preventDefault();
        var content_type = $('input[name="content_type"]').val();
        var model_id = $('input[name="model_id"]').val();
        $.get('create-faq', {'content_type': content_type, 'model_id': model_id})
            .then(function(response) {
                $('.list-faq').append(response);
            }, function(err) {
                notify_error('Ошибка '+ err.status, err.statusText);
            });
    });
    $('.faqForm').on('click', '#send-faq', function (event) {
        event.preventDefault();
        var data = $('.faqForm').serialize();
        $.post('save-faq/', data)
            .then(function(response) {
                notify_success(response, 'Сохранено');
            }, function(err) {
                notify_error('Ошибка '+ err.status, err.statusText);
            });
    });

    $('.faqForm').on('click', '.delete-faq', function (event) {
        event.preventDefault();
        var faq_id = $(this).next().val();
        _this = $(this);
        $.get('del-faq/'+faq_id)
            .then(function(response) {
                notify_success(response, 'Удалено');
                _this.parents('.faq-quant').fadeOut();
            }, function(err) {
                notify_error('Ошибка '+ err.status, err.statusText);
            });
    })
});