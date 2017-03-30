/**
 * Created by varunok on 30.03.17.
 */

        function dell_app(id, _this) {
            $.get('delete/'+id)
                .then(function(response) {
                    _this.fadeOut('slow', function () {
                           _this.remove();
                        });
                    notify_success(0, 'Удалено');
                }, function(err) {
                    notify_error('Ошибка '+ err.status, err.statusText);
                });
        }
