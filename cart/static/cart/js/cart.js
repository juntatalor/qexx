/**
 * Created by Сергей on 15.02.2015.
 */

$(document).ready(function () {

    var spinner;
    var opts = {
      radius: 4,
      width: 2,
      length: 3,
      lines: 11,
      left: '10px'
    };

    function update_cart(data) {
        if (!data.error) {
                $('#cart-items').html(data.html);
                $.get('/cart/summary/', {}, function (data) {
                    $('#cart-widget').html(data.html);
                });
            }
        spinner.stop();
        $('#confirmModal').modal('hide');
    }

    $('#confirmModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget);
        var product_id = button.data('product-id');
        var product_href = button.data('product-href');
        var product_name = button.data('product-name');
        var product_link = $(this).find('#product-link');
        product_link.attr('href', product_href);
        product_link.text(product_name);
        $(this).find('#modalOK').attr('product-id', product_id);
    });

    $('#modalOK').click(function () {
        var product_id = $(this).attr('product-id');
        var product_amount = $(this).attr('product-amount');
        spinner = new Spinner(opts).spin(this);
        $.ajax({
            url: '/cart/remove/',
            type: 'POST',
            data: {product_id: product_id, amount: product_amount}
        }).done(update_cart)
    });

    $('#cart-items').on('click', '#cart-update', function () {
        spinner = new Spinner(opts).spin();
        this.appendChild(spinner.el);
        var cart_items = [];
        $('.cart-product-amount').each(function () {
            cart_items.push({
                product: $(this).data('product-id'),
                amount: $(this).val()
            });
        });
        $.ajax({
            url: '/cart/update/',
            type: 'POST',
            data: {'cart_items': JSON.stringify(cart_items)}
        }).done(update_cart);
    });

});
