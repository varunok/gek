/**
 * Created by varunok on 31.05.17.
 */
$(document).ready(function() {
    // $(document).on('click', '#btn-seo-save', function (event) {
    //     event.preventDefault();
    // });
    $('#seoForm').submit(function(evt) {
        evt.preventDefault();
        var content = CKEDITOR.instances['id_content'].getData();
        var formData = new FormData(this);
        formData.append('content', content);

                $.ajax({
                type: 'POST',
                url: 'seo-save/',
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
    })
});