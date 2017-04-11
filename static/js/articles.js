/**
 * Created by varunok on 28.03.17.
 */
$(document).ready(function() {
    var page = 2;
    $(document).on('click', '.load_more', function (event) {
        event.preventDefault();
        _this = $(this);
        var section = $('input[name="section"]').val();
        $.get('more_pages', {'page': page, 'section': section})
                .then(function(response) {
                    var data = $.parseJSON(response);
                    $('#add-article').append(data.html);
                    page ++;
                    _this.find('span').text(data.obj);
                    if(!data.next){
                        _this.hide()
                    }
                }, function(err) {});
    })
});