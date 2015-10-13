__author__ = 'Сергей'

from shipping.methods import BaseShipment


class PickupDelivery(BaseShipment):

    id = 'PickupDelivery'
    name = 'Самовывоз'
    help_text = 'Вы сами приезжаете и забираете ваш товар из нашего уютного оффиса в центре Москоу-сити'

    @classmethod
    def update_form(cls, form):
        # Удаление недопустимых методов оплаты
        forbidden_gateways = ['CashOnDelivery']
        form.fields['payment'].choices = \
            [(name, v) for name, v in form.fields['payment'].choices if name not in forbidden_gateways]


METHOD = PickupDelivery
