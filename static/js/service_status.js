/**
 * Created by varunok on 31.03.17.
 */
$(document).ready(function() {
    $('.serviceStatus').on('change', 'input[type=checkbox]', function () {
        var data = $(this).parents('.slideThreeForm').serialize();
        $.post('status_service', data)
                .then(function(response) {
                    notify_success(response, 'Успешно');
                }, function(err) {
                    notify_error('Ошибка '+ err.status, err.statusText);
                });
    });

    $('.faqStatus').on('change', 'input[type=checkbox]', function () {
        var data = $(this).parents('.statusFaqForm').serialize();
        $.post('status_faq', data)
                .then(function(response) {
                    notify_success(response, 'Успешно');
                }, function(err) {
                    notify_error('Ошибка '+ err.status, err.statusText);
                });
    });

    $('.repStatus').on('change', 'input[type=checkbox]', function () {
        var data = $(this).parents('.statusRepForm').serialize();
        $.post('status_rep', data)
                .then(function(response) {
                    notify_success(response, 'Успешно');
                }, function(err) {
                    notify_error('Ошибка '+ err.status, err.statusText);
                });
    });

    $('.packetStatus').on('change', 'input[type=checkbox]', function () {
        var data = $(this).parents('.statusPacketForm').serialize();
        $.post('status_packet', data)
                .then(function(response) {
                    notify_success(response, 'Успешно');
                }, function(err) {
                    notify_error('Ошибка '+ err.status, err.statusText);
                });
    });

    $('#delete-image').click(function (event) {
        event.preventDefault();
        var content_type = $(this).next().val();
        var id = $(this).next().next().val();
        var title_image = $(this).next().next().next().val();
        var seo_image = $('input[name="seoImage"]').val();
        var form_image = $('input[name="formImage"]').val();

        _this = $(this);
        $.get('delete-image', {'content_type': content_type, 'id':id,
            'title_image': title_image, 'seo_image': seo_image, 'form_image': form_image})
            .then(function(response) {
                    notify_success(response, 'Успешно');
                    $('#blah').attr("src","second.jpg");
                    _this.fadeOut();
                }, function(err) {
                    notify_error('Ошибка '+ err.status, err.statusText);
                });
    });
    $('#delete-image2').click(function (event) {
        event.preventDefault();
        var content_type = $(this).next().val();
        var id = $(this).next().next().val();
        var title_image = $(this).next().next().next().val();
        _this = $(this);
        $.get('delete-image', {'content_type': content_type, 'id':id, 'title_image': title_image})
            .then(function(response) {
                    notify_success(response, 'Успешно');
                    $('#blah2').attr("src","second.jpg");
                    _this.fadeOut();
                }, function(err) {
                    notify_error('Ошибка '+ err.status, err.statusText);
                });
    })

});