/**
 * Created by varunok on 13.05.17.
 */

var parameter_list_building = {
    type_deal: $('div[name="type_deal"]').eq(0).text() || '--',
    appointment: $('div[name="appointment"]').eq(0).text() || '--',
    district: $('div[name="district"]').eq(0).text() || '--',
    layout: $('div[name="layout"]').eq(0).text() || '--',
    rooms: $('div[name="rooms"]').eq(0).text() || '--',
    price: $('div[name="price"]').eq(0).text() || '--',
    footage: $('div[name="footage"]').eq(0).text() || '--',
    floor: $('div[name="floor"]').eq(0).text() || '--'
};
var string_parameter_list_building = new String(
    'Тип: ' + parameter_list_building.type_deal+'.'+' Назначение: ' + parameter_list_building.appointment+'.'+' Район: ' + parameter_list_building.district+'.'+' Планировка: ' + parameter_list_building.layout+'.'+
    ' Комнат: ' + parameter_list_building.rooms+'.'+' Стоимость: ' + parameter_list_building.price+'.'+' Площадь: ' + parameter_list_building.footage+'.'+' Этаж: ' + parameter_list_building.floor+'.'

);

$('.hid-name-building, input[name="text"]').val(string_parameter_list_building);

var parameter_list_office = {
    type_deal: $('div[name="type_deal"]').eq(0).text() || '--',
    appointment: $('div[name="appointment"]').eq(0).text() || '--',
    // district: $('div[name="district"]').eq(0).text() || '--',
    location: $('div[name="location"]').eq(0).text() || '--',
    entrance: $('div[name="entrance"]').eq(0).text() || '--',
    price: $('div[name="price"]').eq(0).text() || '--',
    footage: $('div[name="footage"]').eq(0).text() || '--',
    floor: $('div[name="floor"]').eq(0).text() || '--'
};
var string_parameter_list_office = new String(
    'Тип: ' + parameter_list_office.type_deal+'.'+' Назначение: ' + parameter_list_office.appointment+'.'+' Расположение: ' + parameter_list_office.location+'.'+
    ' Вход: ' + parameter_list_office.entrance+'.'+' Стоимость: ' + parameter_list_office.price+'.'+' Площадь: ' + parameter_list_office.footage+'.'+' Этаж: ' + parameter_list_office.floor+'.'

);

$('.hid-name-office, input[name="text"]').val(string_parameter_list_office);


var parameter_list_daily = {
    district: $('div[name="district"]').eq(0).text() || '--',
    sleeping_places: $('div[name="sleeping_places"]').eq(0).text() || '--',
    price: $('div[name="price"]').eq(0).text() || '--',
    rooms: $('div[name="rooms"]').eq(0).text() || '--'
};
var string_parameter_list_daily = new String(
    'Район: ' + parameter_list_daily.district+'.'+' Стоимость: ' + parameter_list_daily.price+'.'+' Спальных мест: ' + parameter_list_daily.sleeping_places+'.'+' Кол-во комнат: ' + parameter_list_daily.rooms+'.'

);

$('.hid-name-daily, input[name="text"]').val(string_parameter_list_daily);



var parameter_list_newbuilding = {
    district: $('div[name="district"]').eq(0).text() || '--',
    price: $('div[name="price"]').eq(0).text() || '--',
    total_area: $('div[name="total_area"]').eq(0).text() || '--'
};
var string_parameter_list_newbuilding = new String(
    'Район: ' + parameter_list_newbuilding.district+'.'+' Стоимость: ' + parameter_list_newbuilding.price+'.'+' Площадь квартиры: ' + parameter_list_newbuilding.total_area+'.'

);

$('.hid-name-newbuilding, input[name="text"]').val(string_parameter_list_newbuilding);



var parameter_list_earth = {
    district: $('div[name="district"]').eq(0).text() || '--',
    price: $('div[name="price"]').eq(0).text() || '--',
    area: $('div[name="area"]').eq(0).text() || '--',
    type_area: $('div[name="type_area"]').eq(0).text() || '--'
};
var string_parameter_list_earth = new String(
    'Район: ' + parameter_list_earth.district+'.'+' Стоимость: ' + parameter_list_earth.price+'.'+' Площадь: ' + parameter_list_earth.area+'.'+' Тип участка: ' + parameter_list_earth.type_area+'.'

);

$('.hid-name-earth, input[name="text"]').val(string_parameter_list_earth);

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