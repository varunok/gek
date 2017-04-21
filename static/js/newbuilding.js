/**
 * Created by varunok on 20.04.17.
 */
$(document).ready(function() {
    $('#tab_content_related_object').on('click', '.item-related', function () {
        var object_id = $('#object-id').val();
        var building_id = $(this).children('input').val();
        var _this = $(this);
        $.get('related-building/'+object_id+'/'+building_id)
            .then(function(response) {
                notify_success(response, 'Успешно');
                _this.fadeOut('slow', function () {
                    if(response==='Добавлено'){
                        var block_arrow = _this.children('.arrow-block').remove();
                        block_arrow.children().removeClass('fa-arrow-right').addClass('fa-arrow-left');
                        _this.prepend(block_arrow);
                        $('.item-add').append(_this.fadeIn());
                    }else{
                        var block_arrow = _this.children('.arrow-block').remove();
                        block_arrow.children().removeClass('fa-arrow-left').addClass('fa-arrow-right');
                        _this.append(block_arrow);
                        $('.item-remove').append(_this.fadeIn());
                    }
                });

            }, function(err) {
                notify_error('Ошибка '+ err.status, err.statusText);
            });
    })
});