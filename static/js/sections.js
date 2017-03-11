/**
 *
 * Created by varunok on 12.03.17.
 */

    $(document).ready(function() {
        $(document).on('click', '.del-section', function (event) {
            event.preventDefault();
            var id = $(this).attr('href');
            var _this = $(this).parents('tr');
            notify_confirm(id, _this, 0, 0, dell_app);
        });

        function dell_app(id, _this) {
            $.get('delete/'+id)
                .then(function(response) {
                    _this.fadeOut('slow');
                    notify_success(0, 'Удалено');
                }, function(err) {
                    notify_error('Ошибка '+ err.status, err.statusText);
                });
        }
    });