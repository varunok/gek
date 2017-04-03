/**
 * Created by varunok on 01.04.17.
 */
    $(document).ready(function() {
        $('.statusVideoForm').on('change', 'input[type=checkbox]', function (event) {
            var loop_video_id = $(this).nextAll('.loop_video_id').val();
            var check = $('#id_common-video-content_type-object_id-'+loop_video_id+'-is_enable').prop("checked" ,$(this).prop( "checked" ));
            var data = $(this).parents('.statusVideoForm').serializeArray();
            $.post('status_video', data)
                .then(function(response) {
                    notify_success(response, 'Успешно');
                }, function(err) {
                    notify_error('Ошибка '+ err.status, err.statusText);
                });
        });

        $(document).on('click', '.btn-video', function () {
            _this = $(this);
            var video_id = $(this).next('input').val();
            $.get('modal-video/'+video_id)
                .then(function(response) {
                    _this.next().next().find('.modal-content').html(response);
                }, function(err) {
                    notify_error('Ошибка '+ err.status, err.statusText);
                });
        });

        $(document).on('click', '#send-video', function (event) {
            event.preventDefault();
            var data = $('form[name="videoForm"]').serialize();
            $.post('save-video/', data)
                .then(function(response) {
                    notify_success(response, 'Успешно');
                }, function(err) {
                    notify_error('Ошибка '+ err.status, err.statusText);
                });
        })
    });