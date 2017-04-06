/**
 * Created by varunok on 04.04.17.
 */

$(document).ready(function() {
    $('#galleryForm').submit(function(evt) {
                evt.preventDefault();

                var formData = new FormData(this);

                $.ajax({
                type: 'POST',
                url: 'save-photo/',
                data:formData,
                cache:false,
                contentType: false,
                processData: false,
                success: function(data) {
                    $('.gallery').append(data);
                    notify_success(0, 'Сохранено');
                },
                error: function(data) {
                    notify_error('Ошибка '+ data.status, data.statusText);
                }
                });
            });
    $(document).on('click', '.del-photo', function (event) {
        event.preventDefault();
        _this = $(this);
        var photo_id = $(this).parent().next().val();
        $.get('delete-photo/'+photo_id)
            .then(function(response) {
                notify_success(response, 'Удалено');
                _this.parents('.col-md-55').fadeOut();
            }, function(err) {
                notify_error('Ошибка '+ err.status, err.statusText);
            });
    })
});