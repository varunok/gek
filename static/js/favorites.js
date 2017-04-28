/**
 * Created by varunok on 28.04.17.
 */
$(document).ready(function() {
    $(document).on('click', '.star, .favorite', function () {
        var content_type = $(this).children('input[name="content_type"]').val();
        var object_id = $(this).children('input[name="object_id"]').val();
        $.get('favorites/set/'+content_type+'/'+object_id)
    })
});