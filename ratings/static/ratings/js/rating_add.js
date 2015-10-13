/**
 * Created by Сергей on 07.06.2015.
 */

$(document).ready(function () {

    $('#ratings').on('submit', '#rating-form', function(event) {
        event.preventDefault();
        $.ajax({
            url: '/ratings/add_rating/',
            type: 'POST',
            data: $('#rating-form').serialize()
        }).done(function(data) {
            $('#rating-add').html(data.html)
        })
    })
});
