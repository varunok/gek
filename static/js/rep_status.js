/**
 * Created by varunok on 02.04.17.
 */
$(document).ready(function() {
    $('.repForm').on('click', '#create_rep', function (event) {
        event.preventDefault();
        var content_type = $('input[name="content_type"]').val();
        var model_id = $('input[name="model_id"]').val();
        $.get('create-rep', {'content_type': content_type, 'model_id': model_id})
            .then(function(response) {
                $('.list-rep').append(response);
            }, function(err) {
                notify_error('Ошибка '+ err.status, err.statusText);
            });
    });
    $('.repForm').on('click', '#send-rep', function (event) {
        event.preventDefault();
        var data = $('.repForm').serialize();
        $.post('save-rep/', data)
            .then(function(response) {
                notify_success(response, 'Сохранено');
            }, function(err) {
                notify_error('Ошибка '+ err.status, err.statusText);
            });
    });

    $('.repForm').on('click', '.delete-rep', function (event) {
        event.preventDefault();
        var rep_id = $(this).next().val();
        _this = $(this);
        $.get('del-rep/'+rep_id)
            .then(function(response) {
                notify_success(response, 'Удалено');
                _this.parents('.rep-quant').fadeOut();
            }, function(err) {
                notify_error('Ошибка '+ err.status, err.statusText);
            });
    })
});