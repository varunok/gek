$(document).ready(function() {
    var count = 1
    $('.packets').on('click', '.add-input', function(event) {
        event.preventDefault();
        $(this).parents('.pricing').find('.packetForm').append('<input class="hade-item" name="item-'+count+'" type="text" style="width:100%;">');
        count ++;
    });

    $('.packets').on('click', '.save-input', function(event) {
        event.preventDefault();
        var data = $(this).parents('.pricing').find('.packetForm').serialize();
        var _this = $(this).parents('.pricing').find('.packetForm');
        var _this_ul = $(this).parents('.pricing').find('.list-unstyled');
        $.post('packet-text-save', data)
            .then(function(response) {
                notify_success(response, 'Сохранено');
                var data = _this.serializeArray();
                _this.children('.hade-item').remove();
                var edit_name = _this.parents('.pricing').find('.edit-name');
                console.log(edit_name.val());
                edit_name.parents('.title').html('<h1>'+edit_name.val()+' </h1><i class="fa fa-pencil"></i>');
                for(var i in data){
                    if(data[i].name.search('item') != -1){
                        _this_ul.append('<li>'+data[i].value+'</li>');
                    }
                }
            }, function(err) {
                notify_error('Ошибка '+ err.status, err.statusText);
            });
    });

    $('.append-packet').on('click', '.add-packet', function(event) {
        event.preventDefault();
        var data = $(this).prev('.packetAddForm').serialize();
        var _this = $(this);
        $.post('packet-create', data)
            .then(function(response) {
                _this.parents('.append-packet').html(response);
                notify_success('Успешно', 'Создано');
            }, function(err) {
                notify_error('Ошибка '+ err.status, err.statusText);
            });
    });

    $(document).on('click', '.fa-pencil', function () {
        $(this).prev('h1').html('<input type="text" class="edit-name" style="width: 100%;color: black">');
    });
    $(document).on('keyup', '.edit-name', function () {
        $(this).parents('.pricing').find('input[name="name"]').val($(this).val());
    })
});