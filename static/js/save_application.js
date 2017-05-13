/**
 * Created by varunok on 13.05.17.
 */
$(document).ready(function () {
    $('.add_advert').livequery('click', function () {
                    $('body').addClass('popup');
                    $('#block-webform').fadeIn();
                });
                $('.application').livequery('click', function () {
                    $('body').addClass('popup');
                    $('.block-add-application').fadeIn();
                });
                $('.block-add-repair-sub').livequery('click', function (event) {
                    event.preventDefault();
                    $('body').addClass('popup');
                    $('.block-add-repair').fadeIn();
                });

                $(document).on('click', '.close', function () {
                    $('body').removeClass('popup');
                    $('.block_webform').fadeOut();
                });

    $(document).on('click', '.submit-save-application', function (event) {
                    event.preventDefault();
                    var data = $(this).parents('form').serialize();
                    send_app(data);
            });
        function send_app (data) {
            // $('.block_webform').fadeOut();
            $.post('/save-application/', data)
                .then(function(response) {
                    $('.block_webform').fadeOut();
                    $('body').addClass('popup');
                    $('#webform_confirmation_text').text('Спасибо! Ваша заявка отправлена!');
                    $('#block-webform-confirm').fadeIn();
                }, function(err) {
                    $('.block_webform').fadeOut();
                    $('body').addClass('popup');
                    $('#webform_confirmation_text').text('Ошибка. Попробуйте позже.');
                    $('#block-webform-confirm').fadeIn();
                });
        }
});