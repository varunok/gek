/**
 * Created by varunok on 25.05.17.
 */
$(document).ready(function() {
    $(document).on('click', '.btn-partner-create', function (event) {
        event.preventDefault();
        $('.table-partners').fadeOut('300', function () {
            $('.partner-create').fadeIn();
        });
    });
    $(document).on('click', '.btn-partner-list', function (event) {
        event.preventDefault();
        $('.partner-create').fadeOut('300', function () {
            $('.table-partners').fadeIn();
            $('form[name="partnerForm"]').find("input[type=text], input[type=email], textarea").val("");
        });
        var content_type = $('form[name="partnerForm"]').find('input[name="content_type"]').val();
        var object_id = $('form[name="partnerForm"]').find('input[name="object_id"]').val();
        $.get('get-partner-list/'+content_type+'/'+object_id+'/')
            .then(function(response) {
                $('.include-partners').html(response);
                }, function(err) {});
    });
    $(document).on('click', '.btn-save-partner', function (event) {
        event.preventDefault();
        var data = $('form[name="partnerForm"]').serialize();
        $.post('partner/create/', data)
            .then(function(response) {
                notify_success(0, 'Сохранено');
                }, function(err) {
                notify_error('Ошибка '+ data.status, data.statusText + ". "+data.responseText);
            });
    });
    $('.table').on('click', '.del-partner', function (event) {
        event.preventDefault();
        var id = $(this).attr('href');
        var _this = $(this).parents('tr');
        notify_confirm(id, _this, 0, 0, dell_app);
    });

    function dell_app(id, _this) {
        $.get('partner/dell/'+id+'/')
            .then(function(response) {
                _this.fadeOut('slow');
                notify_success(0, 'Удалено');
            }, function(err) {
                notify_error('Ошибка '+ err.status, err.statusText);
            });
    }
    $(document).on('click', '.btn-partner-edit', function (event) {
        event.preventDefault();
        var object_id = $(this).attr('href');
        $('.table-partners').fadeOut('300', function () {
            $('.partner-create').fadeIn();
        });
        $.get('partner/edit/'+object_id+'/')
            .then(function(response) {
                $('.include-form-partners').html(response);
                }, function(err) {});
    })
});