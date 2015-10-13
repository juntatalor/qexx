__author__ = 'Сергей'

from django.db import models
from django.db.models import Sum, Q, F, Case, When, Value
from django.db.models.functions import Coalesce

from cart.models import CartProducts
from products.models import Product, PricedProduct
from orders.models import OrderProducts
from stock.models import ComingProducts, StockRecord, StockOrderProducts
from stock.constants import FIFO, LIFO


def create_sr_main(order, method=FIFO):
    # здесь Raw SQL гораздо эффективнее Django ORM (LEFT OUTER JOIN по двум полям)
    # Запись списаний
    query = ('SELECT * FROM "orders_orderproducts" '
             'LEFT OUTER JOIN "stock_stockorderproducts" '
             'ON "orders_orderproducts"."id" = "stock_stockorderproducts"."order_products_id" '
             'AND "orders_orderproducts"."priced_product_id" = "stock_stockorderproducts"."priced_product_id" '
             'WHERE  "orders_orderproducts"."order_id" = %s '
             'AND "orders_orderproducts"."amount" - COALESCE("stock_stockorderproducts"."distributed_amount", 0) != 0')
    for order_product in OrderProducts.objects.raw(query, [order.id]):
        amount = order_product.amount - (order_product.distributed_amount or 0)
        if amount > 0:
            create_stock_records(order_product, order_product.priced_product, amount, order_product.amount, method)
        else:
            return_products(order_product, order_product.priced_product, abs(amount), order_product.amount, method)


def create_sr_additional(order, method=FIFO):
    # здесь Raw SQL гораздо эффективнее Django ORM (LEFT OUTER JOIN по двум полям)
    # Запись списаний для дополнительных товаров
    query = ('SELECT * FROM "orders_orderproducts" '
             'INNER JOIN "products_pricedproduct" '
             'ON "products_pricedproduct"."id" = "orders_orderproducts"."priced_product_id" '
             'INNER JOIN "products_product" '
             'ON "products_product"."id" = "products_pricedproduct"."product_id" '
             'INNER JOIN "products_packageproduct" '
             'ON "products_product"."id" = "products_packageproduct"."product_id" '
             'LEFT OUTER JOIN "stock_stockorderproducts" '
             'ON "orders_orderproducts"."id" = "stock_stockorderproducts"."order_products_id" '
             'AND "products_packageproduct"."additional_product_id" = "stock_stockorderproducts"."priced_product_id" '
             'WHERE  "orders_orderproducts"."order_id" = %s '
             'AND "orders_orderproducts"."amount" - COALESCE("stock_stockorderproducts"."distributed_amount", 0) != 0')
    for order_product in OrderProducts.objects.raw(query, [order.id]):
        amount = order_product.amount - (order_product.distributed_amount or 0)
        if amount > 0:
            create_stock_records(order_product, order_product.additional_product, amount, order_product.amount, method)
        else:
            return_products(order_product, order_product.additional_product, abs(amount), order_product.amount, method)


def create_stock_records(order_product, priced_product, distribute_amount, amount, method):
    # Количество позиций, которые осталось раскидать по партиям
    amount_left = distribute_amount

    if method == FIFO:
        ordering = 'coming__date_received'
    else:
        # LIFO - последний пришел, первый ушел
        ordering = '-coming__date_received'

    # Остатки по полученным партиям с данным продуктом
    records = ComingProducts.objects. \
        filter(priced_product=priced_product,
               coming__received=True). \
        order_by(ordering). \
        annotate(used=Coalesce(Sum('stockrecord__amount'), 0)). \
        filter(used__lte=F('amount'))

    for record in records:
        if amount_left == 0:
            break

        if amount_left > record.amount:
            distributed_amount = record.amount
            amount_left -= record.amount
        else:
            distributed_amount = amount_left
            amount_left = 0

        # Запись в базу
        StockRecord.objects.create(priced_product=priced_product,
                                   order_products=order_product,
                                   coming_products=record,
                                   amount=distributed_amount)
    StockOrderProducts.objects.update_or_create(order_products=order_product,
                                                priced_product=priced_product,
                                                defaults={'distributed_amount': amount})


def return_products(order_product, priced_product, return_amount, amount, method):
    amount_left = return_amount

    if method == FIFO:
        ordering = 'coming_products__coming__date_received'
    else:
        # LIFO - последний пришел, первый ушел
        ordering = '-coming_products__coming__date_received'

    # Остатки по полученным партиям с данным продуктом
    records = StockRecord.objects. \
        filter(order_products=order_product,
               priced_product=priced_product). \
        order_by(ordering)

    for record in records:
        if amount_left == 0:
            break

        if amount_left >= record.amount:
            amount_left -= record.amount
            record.delete()
        else:
            record.amount -= amount_left
            record.save()
            amount_left = 0

    StockOrderProducts.objects.update_or_create(order_products=order_product,
                                                priced_product=priced_product,
                                                defaults={'distributed_amount': amount})
