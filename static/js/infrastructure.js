/**
 * Created by varunok on 21.04.17.
 */
$(document).ready(function() {
    // $(document).on('click', '#send_infrastructure', function (event) {
    //     event.preventDefault();
    // });
    $('#infrastructureForm').submit(function(evt) {
                evt.preventDefault();

                var formData = new FormData(this);

                $.ajax({
                type: 'POST',
                url: 'save-infrastructure/',
                data:formData,
                cache:false,
                contentType: false,
                processData: false,
                success: function(data) {
                    var data = $.parseJSON(data);
                    notify_success(0, 'Сохранено');
                    if (data.add){
                        $('.infra-add').prepend(data.item)
                    }else{
                        $('.infra-remove').prepend(data.item)
                    }
                },
                error: function(data) {

                    notify_error('Ошибка '+ data.status, data.statusText + ". "+data.responseText);
                }
                });
    });

    $('#tab_infrastructure').on('click', '.item-infra', function () {
        var object_id = $('#object-id').val();
        var infra_id = $(this).children('input[name="infra_id"]').val();
        var content_type = $(this).children('input[name="content_type"]').val();
        var _this = $(this);
        $.get('related-infrastructure/'+content_type+'/'+infra_id+'/'+object_id)
            .then(function(response) {
                notify_success(response, 'Успешно');
                _this.fadeOut('slow', function () {
                    if(response==='Добавлено'){
                        var block_arrow = _this.children('.arrow-block').remove();
                        block_arrow.children().removeClass('fa-arrow-right').addClass('fa-arrow-left');
                        _this.prepend(block_arrow);
                        $('.infra-add').prepend(_this.fadeIn());
                    }else{
                        var block_arrow = _this.children('.arrow-block').remove();
                        block_arrow.children().removeClass('fa-arrow-left').addClass('fa-arrow-right');
                        _this.append(block_arrow);
                        $('.infra-remove').prepend(_this.fadeIn());
                    }
                });

            }, function(err) {
                notify_error('Ошибка '+ err.status, err.statusText);
            });
    })
});