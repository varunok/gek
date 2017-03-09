/**
 * Created by varunok on 07.03.17.
 */
$(document).ready(function() {
    $('.table').on('click', '.del-app', function (event) {
        event.preventDefault();
        var id = $(this).attr('href');
        var _this = $(this).parents('tr');
        notify_confirm(id, _this, 0, 0, dell_app);
    });

    $('.table').on('click', '#del-all-app', function (event) {
        event.preventDefault();
        var _this = $(this).parents('thead').next('tbody');
        notify_confirm(0, _this, 0, 0, dell_app_all);
    });

    function dell_app(id, _this) {
        $.get('app/dell/'+id)
            .then(function(response) {
                _this.fadeOut('slow');
                notify_success(0, 'Удалено');
            }, function(err) {
                notify_error('Ошибка '+ err.status, err.statusText);
            });
    }

    function dell_app_all(id, _this) {
        $.get('app/dell/all')
            .then(function(response) {
                _this.fadeOut('slow');
                notify_success(0, 'Удалено');
            }, function(err) {
                notify_error('Ошибка '+ err.status, err.statusText);
            });
    }
});


