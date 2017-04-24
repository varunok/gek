/**
 * Created by varunok on 24.04.17.
 */
$(document).ready(function() {
    $(document).on('click', '#btn_an', function (event) {
        // event.preventDefault();
        var data = $('#apartment_nextForm').serialize();
        $.post('save-apartment-next/', data)
            .then(function(response) {
                notify_success('Сохранено', 'Успешно');
                $('.modal').modal('hide');
                var data = $.parseJSON(response);
                $('#tbody-item').prepend(data.item);
            }, function(err) {
                notify_error('Ошибка '+ err.status, err.statusText);
            });
    })
});