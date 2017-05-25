/**
 * Created by varunok on 25.05.17.
 */
$(document).ready(function() {
    var page = 1;
    $(document).on('click', '.load_more', function (event) {
        event.preventDefault();
        page ++;
        $.get('', {'page': page})
            .then(function(response) {
                var data = $.parseJSON(response);
                $('.load_more_wrap').remove();
                $('.list-more').append(data.html);
                if(!data.next){
                    $('.load_more_wrap').remove();
                }
            }, function(err) {});
    })
});