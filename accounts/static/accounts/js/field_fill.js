/**
 * Created by Сергей on 13.01.2015.
 */

$(document).ready(function () {

    $('.username_insert a').click(function () {
        var value = $(this).text();
        var input = $('#id_username');
        input.val(value);
    });

});
