/**
 * Created by varunok on 13.05.17.
 */

var parameter_list = {
    type_deal: $('div[name="type_deal"]').eq(0).text() || '--',
    appointment: $('div[name="appointment"]').eq(0).text() || '--',
    district: $('div[name="district"]').eq(0).text() || '--',
    layout: $('div[name="layout"]').eq(0).text() || '--',
    rooms: $('div[name="rooms"]').eq(0).text() || '--',
    price: $('div[name="price"]').eq(0).text() || '--',
    footage: $('div[name="footage"]').eq(0).text() || '--',
    floor: $('div[name="floor"]').eq(0).text() || '--'
};
var string_parameter_list = new String(
    'Тип: ' + parameter_list.type_deal+'.'+' Назначение: ' + parameter_list.appointment+'.'+' Район: ' + parameter_list.district+'.'+' Планировка: ' + parameter_list.layout+'.'+
    ' Комнат: ' + parameter_list.rooms+'.'+' Стоимость: ' + parameter_list.price+'.'+' Площадь: ' + parameter_list.footage+'.'+' Этаж: ' + parameter_list.floor+'.'

);

$('.hid-name, input[name="text"]').val(string_parameter_list);

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
    $(document).on('click', '.open-object-parameter', function (event) {
        event.preventDefault();
        $('body').addClass('popup');
        $('.object-parameter').fadeIn();
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
                    $('#block-webform-confirm').fadeIn().delay(1000).fadeOut('300', function () {
                        $('body').removeClass('popup');
                    });
                }, function(err) {
                    $('.block_webform').fadeOut();
                    $('body').addClass('popup');
                    $('#webform_confirmation_text').text('Ошибка. Попробуйте позже.');
                    $('#block-webform-confirm').fadeIn().delay(1000).fadeOut('300', function () {
                        $('body').removeClass('popup');
                    });
                });
        }
});