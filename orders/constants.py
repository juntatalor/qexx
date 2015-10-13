__author__ = 'Сергей'

# Статус заказа
ORDER_STATUS = {
    'RESERVED': 0,
    'PROCESSING': 1,
    'SHIPPED': 2,
    'RECEIVED': 3,
    'CANCELLED': 4
}

# Статус оплаты
PAYMENT_STATUS = {
    'NOT_PAYED': 0,
    'PAYMENT_PROCESSING': 1,
    'PAYED': 2
}

ORDER_STATUS_CHOICES = (
    (ORDER_STATUS['RESERVED'], 'Заказ получен'),
    (ORDER_STATUS['PROCESSING'], 'Обработка'),
    (ORDER_STATUS['SHIPPED'], 'Заказ отправлен'),
    (ORDER_STATUS['RECEIVED'], 'Заказ получен'),
    (ORDER_STATUS['CANCELLED'], 'Заказ отменен')
)

ORDER_PAYMENT_STATUS_CHOICES = (
    (PAYMENT_STATUS['NOT_PAYED'], 'Не оплачен'),
    (PAYMENT_STATUS['PAYMENT_PROCESSING'], 'Обработка платежа'),
    (PAYMENT_STATUS['PAYED'], 'Оплачен')
)
