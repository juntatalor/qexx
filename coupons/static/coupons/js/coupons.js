/**
 * Created by Сергей on 19.05.2015.
 * ToDo: для Popover не работает сочетание trigger: 'manual' + selector: '...'
 */

var coupon_add_popover = '';
var coupon_timeout;

var popover_options = {
    html: true,
    trigger: 'manual',
    content: function () {
        return coupon_add_popover;
    }
};

function update_coupons(data, popover_options) {
    $('#coupons').html(data.html);
    $('#coupon-add').popover(popover_options);
}

function coupon_remove() {
    $.ajax({
        url: '/coupons/remove_from_cart/',
        type: 'POST',
        data: {coupon: $(this).data('coupon')}
    }).done(function (data) {
        if (!data.error) {
            update_coupons(data, popover_options);
            // checkout.js
            update_checkout();
        }
    });
}

function coupon_add(event) {
    event.preventDefault();
    $.ajax({
        url: '/coupons/add_to_cart/',
        type: 'POST',
        data: {coupon: $('#id-coupon').val()}
    }).done(function (data) {
        if (data.error) {
            coupon_add_popover = data.error;
            $('#coupon-add').popover('show');
            coupon_timeout = setTimeout(function () {
                $('#coupon-add').popover('hide');
            }, 3000);
        } else {
            update_coupons(data, popover_options);
            // checkout.js
            update_checkout();
        }
    });
}

$(document).ready(function () {

    $('#coupon-add').popover(popover_options);
    var coupons = $('#coupons');
    coupons.on('submit', '#coupons-form', coupon_add);
    coupons.on('click', '.coupon-remove', coupon_remove);

});
