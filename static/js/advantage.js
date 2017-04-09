$(document).ready(function() {
    $('#advantageForm').submit(function(evt) {
                evt.preventDefault();

                var formData = new FormData(this);

                $.ajax({
                type: 'POST',
                url: 'save-advantage/',
                data:formData,
                cache:false,
                contentType: false,
                processData: false,
                success: function(data) {
                    $('.gallery').append(data);
                    notify_success(0, 'Сохранено');
                },
                error: function(data) {
                    console.log(data)
                    notify_error('Ошибка '+ data.status, data.statusText + ' '+data.responseText);
                }
                });
            });
})