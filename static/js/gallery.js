/**
 * Created by varunok on 04.04.17.
 */

$(document).ready(function() {
    // $('.galleryForm').on('click', '#send_photo', function (event) {
    //     event.preventDefault();
    //     var data = $('#galleryForm').serialize();
    //     $.post('save-photo', data)
    // })
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

                },
                error: function(data) {

                }
                });
            });
});