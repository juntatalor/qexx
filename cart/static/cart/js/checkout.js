/**
 * Created by Сергей on 12.03.2015.
 */

function update_checkout() {
        $.ajax({
            url: '/cart/update_checkout/',
            type: 'POST',
            data: $('form').serialize()
        }).done(function (data) {
            $('#checkout-form').html(data.html);
        });
    }

$(document).ready(function () {

    $('body').on('change', 'input[name=shipment]:radio', update_checkout);

});