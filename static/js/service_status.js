/**
 * Created by varunok on 31.03.17.
 */
$(document).ready(function() {
    $(document).on('change', 'input[type=checkbox]', function () {
        var data = $(this).parents('.slideThreeForm').serialize();
        $.post('status_service', data)
                .then(function(response) {
                    notify_success(response, 'Успешно');
                }, function(err) {
                    notify_error('Ошибка '+ err.status, err.statusText);
                });
    })
});