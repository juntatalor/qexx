/**
 * Created by Сергей on 12.02.2015.
 * Реализация popover для кнопки корзины
 * При нажатии отправляет ajax на сервер, и при получении ответа показывает
 * сообщение в popover об успешном добавлении или ошибке
 * popover показывается в течение 3 секунд
 * при повторном нажатии не происходит перерисовка, а используется имеющийся popover
 */

var cart_popover_content = {};
var cart_popover_timeout = {};

$(document).ready(function () {

    var default_price = $('#product-price').text();
    var cart_add = $('.cart-add');

    // Изменение для вариативных продуктов
    var var_select = $('#variation-select');
    if (var_select.length) {
        var_select.change(function () {
            var var_option = $(this).find('option:selected');
            $('.variation-amount').hide();
            if (var_option.val()) {
                $('#cart-add').show();
                $('#amount-' + var_option.val()).show();
                $('#product-price').text(var_option.data('price') + ' ' + var_option.data('currency'));
                $('#product-amount').attr('max', var_option.data('amount'));
                cart_add.attr('data-product', var_option.val());
            } else {
                $('#cart-add').hide();
                $('#product-price').text(default_price)
            }
        })
    }

    cart_add.popover({
        trigger: 'manual',
        html: true,
        content: function () {
            return cart_popover_content[$(this).attr("data-product")]
        }
    });

    cart_add.click(function () {

        var product_id = $(this).attr("data-product");
        var amount = $('#product-amount').val();
        var selector = $(this);

        $.ajax({
            url: '/cart/add/',
            type: 'POST',
            data: {
                product_id: product_id,
                amount: amount
            }
        }).done(function (data) {
            if (data.error) cart_popover_content[product_id] = data.error;
            else cart_popover_content[product_id] = data.html;

            if (cart_popover_timeout[product_id]) {
                clearTimeout(cart_popover_timeout[product_id]);
                var popover = selector.data('bs.popover');
                popover.setContent();
                // Возвращает стрелку на место
                popover.$tip.addClass(popover.options.placement);
            } else selector.popover('show');
            cart_popover_timeout[product_id] = setTimeout(function () {
                selector.popover('hide');
                cart_popover_timeout[product_id] = null;
            }, 3000);
            // Обновление виджета корзины
            $.get('/cart/summary/', {}, function (data) {
                $('#cart-widget').html(data.html);
            });
        });

    });

});
