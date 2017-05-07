/**
 * Created by varunok on 10.04.17.
 */
$(document).ready(function() {
    $(document).on('click', '.searh-click', function (event) {
        event.preventDefault();
        var data = $('.search-form').serializeArray();
        runFilter(data);
    });
    function runFilter(that)
    {
        var params = that;
        var uris = [];

        for (var key in params)
        {
            var value = $.trim(params[key].value);
            if(value != '0' && value != '' && params[key].name != 'csrfmiddlewaretoken')
            {
                uris.push(params[key].name);
                uris.push(params[key].value);
            }
        }
        var redirectTo = BASE_URL;
        if(uris.length > 0)
            redirectTo += '/' + uris.join('-');

        location.href = redirectTo;
    }
    $(document).on('click', '.close', function () {
       location.href = $(this).data('href');
    })
});